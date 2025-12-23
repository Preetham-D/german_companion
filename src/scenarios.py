# src/scenarios.py

SCENARIOS = {
    # --- WORK & OFFICE ---
    "small_talk": {
        "name": "☕ Office Kitchen Small Talk",
        "role": "Colleague (Anna)",
        "difficulty": "Easy",
        "initial_prompt": "Hallo! Wie war dein Wochenende? Hast du etwas Schönes gemacht?",
        "prompt_translation": "Hello! How was your weekend? Did you do anything nice?",
        "initial_prompt_audio": "small_talk.mp3"
    },
    "explaining_task": {
        "name": "📊 Daily Standup Update",
        "role": "Project Manager",
        "difficulty": "Medium",
        "initial_prompt": "Kannst du mir bitte kurz erklären, was du gestern am Projekt gemacht hast?",
        "prompt_translation": "Can you please briefly explain what you did on the project yesterday?",
        "initial_prompt_audio": "explaining_task.mp3"
    },
    "asking_help": {
        "name": "🆘 Asking for Tech Support",
        "role": "IT Specialist",
        "difficulty": "Hard",
        "initial_prompt": "Ich sehe, du hast Probleme mit der Software. Wie genau kann ich dir helfen?",
        "prompt_translation": "I see you are having trouble with the software. How exactly can I help you?",
        "initial_prompt_audio": "asking_help.mp3"
    },
    "job_interview": {
        "name": "💼 Job Interview Question",
        "role": "HR Manager",
        "difficulty": "Hard",
        "initial_prompt": "Erzählen Sie mir bitte ein wenig über sich selbst. Warum wollen Sie diesen Job?",
        "prompt_translation": "Please tell me a little bit about yourself. Why do you want this job?",
        "initial_prompt_audio": "job_interview.mp3"
    },

    # --- DAILY LIFE ---
    "ordering_food": {
        "name": "🥐 Ordering at a Bakery",
        "role": "Baker",
        "difficulty": "Easy",
        "initial_prompt": "Guten Morgen! Was darf es heute für Sie sein?",
        "prompt_translation": "Good morning! What can I get for you today?",
        "initial_prompt_audio": "ordering_food.mp3"
    },
    "train_ticket": {
        "name": "🚆 Buying a Train Ticket",
        "role": "Ticket Agent",
        "difficulty": "Medium",
        "initial_prompt": "Hallo. Wohin möchten Sie reisen und haben Sie eine BahnCard?",
        "prompt_translation": "Hello. Where would you like to travel to, and do you have a BahnCard?",
        "initial_prompt_audio": "train_ticket.mp3"
    },
    "doctor_visit": {
        "name": "🩺 At the Doctor",
        "role": "Doctor",
        "difficulty": "Hard",
        "initial_prompt": "Guten Tag. Welche Beschwerden haben Sie heute?",
        "prompt_translation": "Good day. What symptoms do you have today?",
        "initial_prompt_audio": "doctor_visit.mp3"
    }
}

def get_scenario_names():
    return [data["name"] for key, data in SCENARIOS.items()]

def get_scenario_by_name(name):
    for key, data in SCENARIOS.items():
        if data["name"] == name:
            return data
    return None