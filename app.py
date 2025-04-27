# import streamlit as st
# import pdfplumber
# from googletrans import Translator
# from gtts import gTTS
# import os
# import tempfile
# import uuid
# import zipfile
# from io import BytesIO

# # Set Streamlit page config
# st.set_page_config(page_title="Textbook to Audio Lessons", page_icon="📚", layout="wide")

# # Initialize translator
# translator = Translator()

# # Title
# st.title("📚 Textbook to Bite-Sized Audio Lessons")

# # File uploader
# uploaded_file = st.file_uploader("Upload a textbook (PDF)", type=["pdf"])

# if uploaded_file is not None:
#     # Extract text from PDF
#     st.info("Extracting text from the uploaded PDF...")
#     extracted_text = ""
#     with pdfplumber.open(uploaded_file) as pdf:
#         for page in pdf.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 extracted_text += page_text + " "

#     if extracted_text.strip() == "":
#         st.error("No text could be extracted from the PDF. Please try another file.")
#     else:
#         st.success("Text extraction complete!")

#         # Language selection
#         lang = st.selectbox("Choose Target Language", (
#             ("hi", "Hindi"), 
#             ("ta", "Tamil"),
#             ("te", "Telugu"),
#             ("kn", "Kannada"),
#             ("gu", "Gujarati"),
#             ("ml", "Malayalam"),
#             ("mr", "Marathi"),
#             ("bn", "Bengali")
#         ), format_func=lambda x: x[1])

#         # Chunk size selection
#         chunk_size = st.slider("Select number of sentences per chunk", 1, 5, 2)

#         # Button to start processing
#         if st.button("Generate Audio Lessons 🚀"):
#             st.info("Processing, please wait...")

#             # Split text into sentences (basic split using '.')
#             sentences = extracted_text.split('.')
#             sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

#             # Group sentences into chunks
#             chunks = []
#             for i in range(0, len(sentences), chunk_size):
#                 chunk = '. '.join(sentences[i:i+chunk_size]) + '.'
#                 chunks.append(chunk)

#             # Temporary folder to store audio files
#             temp_dir = tempfile.mkdtemp()
#             audio_files = []

#             st.success(f"Total {len(chunks)} bite-sized lessons created!")

#             # Process each chunk
#             for idx, chunk in enumerate(chunks):
#                 try:
#                     # Translate the chunk
#                     translated_text = translator.translate(chunk, dest=lang[0]).text

#                     # Generate audio
#                     tts = gTTS(text=translated_text, lang=lang[0])
#                     filename = os.path.join(temp_dir, f"lesson_{idx+1}.mp3")
#                     tts.save(filename)
#                     audio_files.append(filename)

#                     # Display audio player
#                     st.subheader(f"Lesson {idx+1}")
#                     st.audio(filename)

#                 except Exception as e:
#                     st.error(f"Error processing chunk {idx+1}: {e}")

#             st.success("All audio lessons are ready! 🎧")

#             # --- New: Create ZIP File ---
#             if audio_files:
#                 zip_buffer = BytesIO()
#                 with zipfile.ZipFile(zip_buffer, "w") as zip_file:
#                     for file_path in audio_files:
#                         zip_file.write(file_path, arcname=os.path.basename(file_path))
#                 zip_buffer.seek(0)

#                 st.download_button(
#                     label="📥 Download All Lessons as ZIP",
#                     data=zip_buffer,
#                     file_name="audio_lessons.zip",
#                     mime="application/zip"
#                 )
# else:
#     st.warning("Please upload a PDF textbook file to start.")



import streamlit as st
import pdfplumber
from googletrans import Translator
from gtts import gTTS
import os
from io import BytesIO

import concurrent.futures  # <-- add this at top of file with imports

# Function to translate a chunk (needed for multithreading)
def translate_chunk(chunk, target_lang):
    return translator.translate(chunk, dest=target_lang).text

# Set Streamlit page config
st.set_page_config(page_title="Full Textbook to Single Audio", page_icon="🎧", layout="wide")

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
