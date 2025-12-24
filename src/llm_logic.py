import os
import json
import logging
import re
import sys
from groq import Groq
from dotenv import load_dotenv

# --- 1. Fix Windows Console Encoding ---
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# --- 2. Logging Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("debug.log", encoding="utf-8"), 
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def clean_json_string(raw_string):
    clean_str = raw_string.strip()
    if clean_str.startswith("```"):
        clean_str = re.sub(r"^```json|^```", "", clean_str)
        clean_str = re.sub(r"```$", "", clean_str)
    return clean_str.strip()

def analyze_response(user_text, scenario):
    logger.info(f"Starting analysis for: {scenario['name']}")
    
    system_prompt = f"""
    You are a helpful German language tutor for NURSES. 
    The user is practicing a scenario: "{scenario['name']}".
    The role of the other person is: "{scenario['role']}".
    The prompt was: "{scenario['initial_prompt']}".
    
    Analyze the User's German response.
    
    Output strictly valid JSON with these keys:
    - "transcript_corrected": (String) User's text with spelling fixed.
    - "translation": (String) English translation of what the user said.
    - "score": (Integer) 0-100 relevance/grammar score.
    - "feedback": (String) Constructive feedback strictly IN ENGLISH.
    - "better_response": (String) A native-level German phrasing (SBAR or professional style).
    - "better_response_translation": (String) English translation of the better_response.
    
    IMPORTANT: Return ONLY the JSON object. No markdown.
    """

    user_prompt = f"User's Response: {user_text}"

    max_retries = 2
    for attempt in range(max_retries):
        try:
            logger.info(f"Sending request to Groq (Attempt {attempt + 1})...")
            
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
            cleaned_content = clean_json_string(raw_content)
            
            result_json = json.loads(cleaned_content)
            
            # Updated keys to include the new translation field
            required_keys = ["transcript_corrected", "translation", "score", "feedback", "better_response", "better_response_translation"]
            for key in required_keys:
                if key not in result_json:
                    result_json[key] = "-"
            
            return result_json

        except Exception as e:
            logger.error(f"API Error on attempt {attempt + 1}: {e}")

    return {
        "error": "Failed after retries",
        "transcript_corrected": user_text,
        "translation": "System Error",
        "score": 0,
        "feedback": "System Error: Could not analyze.",
        "better_response": "-",
        "better_response_translation": "-"
    }