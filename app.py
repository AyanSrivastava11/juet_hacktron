import streamlit as st
import pdfplumber
from googletrans import Translator
from gtts import gTTS
import os
from io import BytesIO

import concurrent.futures  # <-- add this at top of file with imports


def main():
    st.title("🎧 Textbook to Audio Converter App")
    st.write("""
    Upload your textbook PDF, select a regional language, and generate bite-sized audios easily! 🚀
    """)

# Function to translate a chunk (needed for multithreading)
def translate_chunk(chunk, target_lang):
    return translator.translate(chunk, dest=target_lang).text

# Set Streamlit page config
# st.set_page_config(page_title="Full Textbook to Single Audio", page_icon="🎧", layout="wide")

# Initialize translator
translator = Translator()

# Title
st.title("🎧 Textbook to Single Full Audio")

# Function to split text into chunks
def split_text(text, max_length=4000):
    words = text.split()
    chunks = []
    chunk = ""
    for word in words:
        if len(chunk) + len(word) + 1 <= max_length:
            chunk += " " + word
        else:
            chunks.append(chunk.strip())
            chunk = word
    if chunk:
        chunks.append(chunk.strip())
    return chunks

# File uploader
uploaded_file = st.file_uploader("Upload a textbook (PDF)", type=["pdf"])

if uploaded_file is not None:
    # Extract text from PDF
    st.info("Extracting text from the uploaded PDF...")
    extracted_text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text + " "

    if extracted_text.strip() == "":
        st.error("No text could be extracted from the PDF. Please try another file.")
    else:
        st.success("Text extraction complete!")

        # Language selection
        lang = st.selectbox("Choose Target Language", (
            ("hi", "Hindi"), 
            ("ta", "Tamil"),
            ("te", "Telugu"),
            ("kn", "Kannada"),
            ("gu", "Gujarati"),
            ("ml", "Malayalam"),
            ("mr", "Marathi"),
            ("bn", "Bengali")
        ), format_func=lambda x: x[1])

        if st.button("Generate Full Audio 🚀"):
            with st.spinner('Translating and Generating Audio... Please wait!'):
                try:
                    # Split into manageable chunks
                    text_chunks = split_text(extracted_text, max_length=4000)

                    # ✅ NEW: Translate chunks in parallel
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        futures = [executor.submit(translate_chunk, chunk, lang[0]) for chunk in text_chunks]
                        translated_chunks = [future.result() for future in concurrent.futures.as_completed(futures)]

                    # Combine all translated chunks
                    translated_text = " ".join(translated_chunks)

                    # Generate audio as usual
                    tts = gTTS(text=translated_text, lang=lang[0])
                    audio_buffer = BytesIO()
                    tts.write_to_fp(audio_buffer)
                    audio_buffer.seek(0)

                    st.success("Audio generated successfully! 🎧")

                    st.audio(audio_buffer, format="audio/mp3")

                    st.download_button(
                        label="📥 Download Full Audio",
                        data=audio_buffer,
                        file_name="full_textbook_audio.mp3",
                        mime="audio/mp3"
                    )

                except Exception as e:
                    st.error(f"Error during processing: {e}")

                    # Generate audio
                    tts = gTTS(text=translated_text, lang=lang[0])

                    # Save to in-memory buffer
                    audio_buffer = BytesIO()
                    tts.write_to_fp(audio_buffer)
                    audio_buffer.seek(0)

                    st.success("Audio generated successfully! 🎧")

                    # Audio Player
                    st.audio(audio_buffer, format="audio/mp3")

                    # Download Button
                    st.download_button(
                        label="📥 Download Full Audio",
                        data=audio_buffer,
                        file_name="full_textbook_audio.mp3",
                        mime="audio/mp3"
                    )

                except Exception as e:
                    st.error(f"Error during processing: {e}")

else:
    st.warning("Please upload a PDF textbook file to start.")
