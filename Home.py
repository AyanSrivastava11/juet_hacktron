import streamlit as st
import app  # Your existing App.py
import os
import team  # Your existing Team.py

# Page Config (ONLY here!)
st.set_page_config(page_title="Textbook to Audio Converter", page_icon="📚", layout="wide")

# ---- Sidebar Navigation ----
st.sidebar.title("📚 Menu")
page = st.sidebar.radio("Go to", ["🏠 Home", "🛠 App", "👥 About Us"])

# ---- Page Routing ----
if page == "🏠 Home":
    st.title("🏠 Welcome to Textbook to Audio Converter")
    st.markdown("Bridging language barriers with **technology!**")
    st.markdown("""
        ---
        ## 📖 About This Project
        Convert textbooks into **regional language audio lessons** easily and quickly!

        ---
        ## 🎯 How It Works
        1. Upload a textbook (PDF file)
        2. Choose your target language
        3. Generate full audio 📥 or bite-sized audios 🎧
        4. Download and listen anytime!

        ---
        """)
    st.markdown("### 📜 Project Overview")
    st.markdown("""
        This project aims to convert textbooks into audio format in various regional languages. 
        It uses **Google Text-to-Speech** for audio generation and **Streamlit** for the web interface.
    """)
elif page == "🛠 App":
    app.main()

elif page == "👥 About Us":
    st.title("👥 About Us")
    team.show_team_page()
