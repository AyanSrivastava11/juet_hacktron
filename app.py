 
import streamlit as st
import pdfplumber
from googletrans import Translator
from gtts import gTTS
import os
import tempfile
import uuid

# Set Streamlit page config
st.set_page_config(page_title="Textbook to Audio Lessons", page_icon="📚", layout="wide")

# Initialize translator
translator = Translator()

# Title
st.title("📚 Textbook to Bite-Sized Audio Lessons")

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

        # Chunk size selection
        chunk_size = st.slider("Select number of sentences per chunk", 1, 5, 2)

        # Button to start processing
        if st.button("Generate Audio Lessons 🚀"):
            st.info("Processing, please wait...")

            # Split text into sentences (basic split using '.')
            sentences = extracted_text.split('.')
            sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

            # Group sentences into chunks
            chunks = []
            for i in range(0, len(sentences), chunk_size):
                chunk = '. '.join(sentences[i:i+chunk_size]) + '.'
                chunks.append(chunk)

            # Temporary folder to store audio files
            temp_dir = tempfile.mkdtemp()

            st.success(f"Total {len(chunks)} bite-sized lessons created!")

            # Process each chunk
            for idx, chunk in enumerate(chunks):
                try:
                    # Translate the chunk
                    translated_text = translator.translate(chunk, dest=lang[0]).text

                    # Generate audio
                    tts = gTTS(text=translated_text, lang=lang[0])
                    filename = os.path.join(temp_dir, f"lesson_{idx+1}_{uuid.uuid4().hex}.mp3")
                    tts.save(filename)

                    # Display audio player
                    st.subheader(f"Lesson {idx+1}")
                    st.audio(filename)

                except Exception as e:
                    st.error(f"Error processing chunk {idx+1}: {e}")

            st.success("All audio lessons are ready! 🎧")

else:
    st.warning("Please upload a PDF textbook file to start.")
