import os
from gtts import gTTS  # <--- FIXED: 'gtts' must be lowercase
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def text_to_speech_file(text):
    """Generates MP3 audio from text using Google TTS."""
    try:
        tts = gTTS(text=text, lang='de')
        file_path = "temp_prompt.mp3"
        tts.save(file_path)
        return file_path
    except Exception as e:
        print(f"TTS Error: {e}")
        return None

def transcribe_audio(audio_bytes):
    """Sends audio bytes to Groq (Whisper) for transcription."""
    try:
        # Create a temporary file for the API
        with open("temp_input.wav", "wb") as f:
            f.write(audio_bytes)
            
        with open("temp_input.wav", "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(file.name, file.read()),
                model="whisper-large-v3",
                response_format="json",
                language="de",
                temperature=0.0
            )
        return transcription.text
    except Exception as e:
        return f"Error transcribing: {str(e)}"