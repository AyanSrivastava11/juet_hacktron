import streamlit as st
import pdfplumber
from googletrans import Translator
from gtts import gTTS
from io import BytesIO
import concurrent.futures

def main():
    st.title("🎧 Textbook to Audio Converter App")
    st.write("""
    Upload your textbook PDF, select a regional language, and generate bite-sized audios easily! 🚀
    """)

    translator = Translator()

    uploaded_file = st.file_uploader("Upload a textbook (PDF)", type=["pdf"])

    if uploaded_file is not None:
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

            lang = st.selectbox("Choose Target Language", (
                ("hi", "Hindi"), 
                ("ta", "Tamil"),
                ("te", "Telugu"),
                ("kn", "Kannada"),
                ("gu", "Gujarati"),
                ("ml", "Malayalam"),
                ("mr", "Marathi"),
                ("bn", "Bengali"),
                ("pa", "Punjabi"),
                ("ur", "Urdu"),
                ("or", "Odia"),
                ("en", "English"),
                ("es", "Spanish"),
                ("fr", "French"),
                ("de", "German"),
                ("it", "Italian"),
                ("ja", "Japanese"),
                ("zh-cn", "Chinese (Simplified)"),
                ("zh-tw", "Chinese (Traditional)"),
                ("ar", "Arabic"),
                ("pt", "Portuguese"),
                ("ru", "Russian"),
                ("tr", "Turkish"),
                ("th", "Thai"),
                ("vi", "Vietnamese"),
                ("id", "Indonesian"),
                ("sw", "Swahili"),
                ("fi", "Finnish"),
            ), format_func=lambda x: x[1])

            if st.button("Generate Full Audio 🚀"):
                with st.spinner('Translating and Generating Audio... Please wait!'):
                    try:
                        text_chunks = split_text(extracted_text, max_length=4000)

                        with concurrent.futures.ThreadPoolExecutor() as executor:
                            futures = [executor.submit(translate_chunk, chunk, lang[0]) for chunk in text_chunks]
                            translated_chunks = [future.result() for future in concurrent.futures.as_completed(futures)]

                        translated_text = " ".join(translated_chunks)

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

# Helper Functions
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

def translate_chunk(chunk, target_lang):
    translator = Translator()
    return translator.translate(chunk, dest=target_lang).text
