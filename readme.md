# 🎤 Voice Messege (AI Voice Assistant)

A simple yet powerful **Python-based Voice Assistant** project.  
It can recognize your voice, respond with speech, and perform useful tasks like telling the time/date, setting timers, playing music, opening apps, and even cracking jokes!  

---

## ✨ Features
- 🗣️ **Speech Recognition** (powered by [Vosk](https://alphacephei.com/vosk/))
- 🔊 **Text-to-Speech** responses
- ⏰ **Time & Date queries**
- ⏱️ **Stopwatch & Timer**
- 🎵 **Play / Stop Music**
- 📒 **Remember your name** (memory feature)
- 📂 **Open Apps** (Notepad, Calculator, etc.)
- 😂 **Random Jokes**

---

## 📂 Project Structure
voice_messege/
│── main.py # Entry point of the assistant
│── assistant.py # Core assistant logic
│── requirements.txt # Dependencies
│── README.md # Project Documentation
│
├── voice/
│ ├── recognizer.py # Handles speech recognition
│ └── speaker.py # Handles text-to-speech
│
├── features/
│ ├── time_date.py
│ ├── stopwatch.py
│ ├── timer.py
│ ├── apps.py
│ ├── music.py
│ ├── memory.py
│ └── jokes.py
│
├── assets/
│ └── music/ # Store music files here
│
└── vosk-model-small-en-in-0.4/ # Speech recognition model

yaml
Copy
Edit

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/voice_messege.git
   cd voice_messege
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Download the Vosk Model (already included here as vosk-model-small-en-in-0.4).

▶️ Usage
Run the assistant:

bash
Copy
Edit
python main.py
Example commands:

"What is the time?"

"Start stopwatch"

"Stop stopwatch"

"Set timer for 1 minute"

"Play music"

"Open notepad"

"Tell me a joke"

"Exit"

🚀 Future Improvements
Add weather updates 🌦️

Integrate with ChatGPT API for smarter conversations 🤖

Add support for more languages 🌍

👨‍💻 Author
Developed with ❤️ using Python 3.12 and Vosk.
