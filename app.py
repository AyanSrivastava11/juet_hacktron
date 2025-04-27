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