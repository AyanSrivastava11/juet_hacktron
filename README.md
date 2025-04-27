# juet_hacktron -  Team Code_red

# 📚 Textbook to Audio Converter (with Translation) 🚀

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange?logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Convert uploaded PDF textbooks into **translated audio** in multiple languages!  
Built with **Streamlit**, **Google Translate**, and **gTTS**.

---

## ✨ Features

- 📄 Upload any **PDF file**.
- 📚 **Extract text** automatically using `pdfplumber`.
- 🌐 **Translate** the extracted text into multiple languages (e.g., Hindi, Tamil, French, Spanish, etc.).
- 🔊 **Generate audio** from the translated text using **Google Text-to-Speech (gTTS)**.
- 🎧 **Listen to the audio** inside the app.
- 📥 **Download the generated audio** as `.mp3`.
- 💾 (Optional) **Save** the generated audio on the server.

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/textbook-audio-converter.git
cd textbook-audio-converter

# 2. Install the required Python libraries
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
```

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) — For creating the web app UI.
- [pdfplumber](https://github.com/jsvine/pdfplumber) — For extracting text from PDFs.
- [googletrans](https://pypi.org/project/googletrans/) — For translating text chunks.
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) — For generating audio files.
- [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO) — For handling audio in memory.

---

## 📚 How It Works

1. **Upload a PDF file** inside the app.
2. **Text is extracted** from the PDF using `pdfplumber`.
3. The text is **split** into manageable chunks (≤4000 characters).
4. Each chunk is **translated** to the selected target language using `googletrans`.
5. All translated chunks are **joined together**.
6. The final text is **converted to audio** using `gTTS`.
7. The audio is:
   - Streamed live for preview 🎧
   - Available for download as `.mp3` 📥
   - Optionally saved locally on the server 💾

## 🌍 Supported Languages

| Language   | Code  |
|------------|-------|
| Hindi      | `hi`  |
| Tamil      | `ta`  |
| Telugu     | `te`  |
| Kannada    | `kn`  |
| Gujarati   | `gu`  |
| Malayalam  | `ml`  |
| Marathi    | `mr`  |
| Bengali    | `bn`  |
| French     | `fr`  |
| Spanish    | `es`  |
| German     | `de`  |
| Italian    | `it`  |
| Chinese    | `zh-cn` |
| Japanese   | `ja`  |
| Korean     | `ko`  |

_(You can easily add more languages in the code!)_

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contribution

Contributions are welcome!  
Feel free to **fork**, **submit issues**, or **create pull requests**.  
Let's build something amazing together! 🚀

---

## 👨‍💻 Author

Made with ❤️ by **Ayan Srivastava**, **Aditi Singh**, **Aditi Gupta**

---

## 📌 Notes

- Make sure your PDF is **text-based** (not scanned images).
- **Google Translate** and **gTTS** require an **internet connection** to work properly.
- This app is suitable for **small to medium-sized PDFs** (~less than 50 pages recommended).


## 📂 Project Structure

```plaintext
/textbook-audio-converter
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── (any additional modules or utils)
