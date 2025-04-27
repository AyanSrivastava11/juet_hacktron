import streamlit as st
import app  # Your existing App.py
import os
import team  # Your existing Team.py

# Page Config (ONLY here!)
st.set_page_config(page_title="Textbook to Audio Converter", page_icon="📚", layout="wide")

# ---- Sidebar Navigation ----
st.sidebar.title("📚 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🛠 App", "👥 About Us"])

# ---- Page Routing ----
if page == "🏠 Home":
    st.title("🏠 Welcome to Textbook to Audio Converter")
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
    # st.image("https://cdn.pixabay.com/photo/2017/01/31/19/15/book-2022464_960_720.png", width=600)

elif page == "🛠 App":
    app.main()

elif page == "👥 About Us":
    st.title("👥 About Us")
    team.show_team_page()
