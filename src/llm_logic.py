import os
import json
import logging
from groq import Groq
from dotenv import load_dotenv

# --- 1. Logging Configuration ---
# This sets up logging to BOTH a file (debug.log) and the Console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# --- 2. Load Config ---
load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

# Debug check: Print status of API key (without revealing it)
if not api_key:
    logger.critical("CRITICAL: GROQ_API_KEY is missing from .env file!")
else:
    logger.info(f"API Key loaded. Length: {len(api_key)} characters.")

client = Groq(api_key=api_key)

def analyze_response(user_text, scenario):
    logger.info(f"Starting analysis for scenario: {scenario['name']}")
    logger.info(f"User Input: {user_text}")

    system_prompt = f"""
    You are a helpful German language tutor. 
    The user is practicing a scenario: "{scenario['name']}".
    The role of the other person is: "{scenario['role']}".
    The context/prompt given to the user was: "{scenario['initial_prompt']}".
    
    Analyze the User's German response provided below.
    
    Output strictly valid JSON with these keys:
    - "transcript_corrected": (String) The user's text with any minor spelling corrections.
    - "translation": (String) English translation of what the user said.
    - "score": (Integer) 0-100 relevance and grammar score.
    - "feedback": (String) A short, encouraging tip in English on grammar or vocabulary.
    - "better_response": (String) A more natural/native German way to say it.
    
    Do not add any markdown formatting (like ```json). Just the raw JSON string.
    """

    user_prompt = f"User's Response: {user_text}"

    try:
        logger.info("Sending request to Groq API...")
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
            response_format={"type": "json_object"} 
        )
        
        raw_content = completion.choices[0].message.content
        logger.info("Groq response received. Parsing JSON...")
        
        result_json = json.loads(raw_content)
        
        # Validation Loop
        required_keys = ["transcript_corrected", "translation", "score", "feedback", "better_response"]
        for key in required_keys:
            if key not in result_json:
                logger.warning(f"Missing key in JSON: {key}. Filling with placeholder.")
                result_json[key] = "-"
        
        logger.info("Analysis successful.")
        return result_json

    except Exception as e:
        # This prints the EXACT error to your terminal
        logger.error("❌ CRITICAL ERROR IN ANALYZE_RESPONSE:", exc_info=True)
        
        return {
            "error": str(e),
            "transcript_corrected": user_text,
            "translation": "Error: Could not translate.",
            "score": 0,
            "feedback": f"System Error: {str(e)}",
            "better_response": "-"
        }