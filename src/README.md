# 🇩🇪 German AI Companion (Prototype)

A lightweight, conversational AI prototype designed to help professionals practice "survival German" and office scenarios. This tool provides a safe space to speak, offering instant feedback on grammar, vocabulary, and relevance.

Built for the **BorderPlus AI Product Manager Assignment**.

## 🚀 Features

* **Real-world Scenarios:** Practice specific situations like "Small Talk," "Job Interview," or "Ordering at a Café."
* **Voice Interaction:** Listens to your German speech and transcribes it using **Whisper V3**.
* **Instant AI Feedback:** Powered by **Llama 3.3 (70B)** to provide:
    * ✅ Corrected Transcript
    * 📊 Relevance Score (0-100)
    * 🇬🇧 English Translation
    * 💡 Improvement Tips & Native Phrasing
* **Audio Prompts:** Hear the scenario context spoken aloud (Text-to-Speech).

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Python)
* **LLM Intelligence:** [Groq API](https://groq.com/) (running Llama 3.3 70B Versatile)
* **Speech-to-Text:** Groq Whisper V3
* **Text-to-Speech:** gTTS (Google Text-to-Speech)
* **Language:** Python 3.9+

## 📂 Project Structure

```text
german-companion/
├── src/
│   ├── app.py              # Main application UI
│   ├── llm_logic.py        # AI Analysis Logic (Groq/Llama 3)
│   ├── audio_utils.py      # Audio processing (STT/TTS)
│   └── scenarios.py        # Database of roleplay scenarios
├── .env                    # API Keys (Not committed)
├── requirements.txt        # Dependencies
└── README.md

⚙️ Setup & Installation
1. Clone the Repository
Bash

git clone [https://github.com/YourUsername/german-companion.git](https://github.com/YourUsername/german-companion.git)
cd german-companion
2. Install Dependencies
It is recommended to use a virtual environment (venv).

Bash

pip install -r requirements.txt
3. Configure API Key
Get a free API Key from the Groq Console.

Create a file named .env in the root folder.

Add your key inside:

Plaintext

GROQ_API_KEY=gsk_your_actual_api_key_here
4. Run the App
Make sure you are in the root directory (german-companion), then run:

Bash

streamlit run src/app.py
The app will open automatically in your browser at http://localhost:8501.

🧪 How to Use
Select a Scenario from the sidebar (e.g., "Ordering at a Bakery").

Listen to the prompt from the AI character.

Click "Start Recording" and speak your response in German.

Wait a few seconds for the AI to analyze your speech.

Review your Score and Better Response suggestions.