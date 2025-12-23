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
    },

    # ==========================================
    # 1. WARD DUTY (General Patient Care)
    # ==========================================
    "ward_admission": {
        "name": "🏥 Ward: Patient Admission",
        "role": "Patient (Herr Müller)",
        "difficulty": "Medium",
        "initial_prompt": "Guten Tag. Ich bin etwas nervös. Was passiert denn jetzt als Nächstes mit mir?",
        "prompt_translation": "Hello. I am a bit nervous. What happens next with me?",
        "initial_prompt_audio": "ward_admission.mp3"
    },
    "ward_pain": {
        "name": "💊 Ward: Pain Management",
        "role": "Patient (Frau Weber)",
        "difficulty": "Easy",
        "initial_prompt": "Schwester, mein Bein tut wieder sehr weh. Die letzte Tablette hat nicht geholfen.",
        "prompt_translation": "Nurse, my leg hurts a lot again. The last pill didn't help.",
        "initial_prompt_audio": "ward_pain.mp3"
    },
    "ward_hygiene": {
        "name": "uD83DuDEC0 Ward: Morning Hygiene",
        "role": "Patient (Elderly)",
        "difficulty": "Medium",
        "initial_prompt": "Ich schaffe es heute nicht alleine ins Bad. Können Sie mir beim Waschen helfen?",
        "prompt_translation": "I can't make it to the bathroom alone today. Can you help me wash?",
        "initial_prompt_audio": "ward_hygiene.mp3"
    },

    # ==========================================
    # 2. ICU (Intensive Care Unit)
    # ==========================================
    "icu_alarm": {
        "name": "🚨 ICU: Monitoring Alarm",
        "role": "Senior Nurse",
        "difficulty": "Hard",
        "initial_prompt": "Der Monitor bei Bett 3 alarmiert. Die Sauerstoffsättigung fällt. Was machst du?",
        "prompt_translation": "The monitor at Bed 3 is alarming. Oxygen saturation is dropping. What do you do?",
        "initial_prompt_audio": "icu_alarm.mp3"
    },
    "icu_sedation": {
        "name": "💤 ICU: Sedation Check",
        "role": "Anesthesiologist",
        "difficulty": "Hard",
        "initial_prompt": "Der Patient wirkt unruhig. Wie ist der aktuelle RASS-Score und sollen wir das Propofol erhöhen?",
        "prompt_translation": "The patient seems restless. What is the current RASS score and should we increase the Propofol?",
        "initial_prompt_audio": "icu_sedation.mp3"
    },
    "icu_transfer": {
        "name": "🛏️ ICU: Transfer Report",
        "role": "Receiving Nurse",
        "difficulty": "Medium",
        "initial_prompt": "Ich übernehme den Patienten jetzt. Hat er heute schon Stuhlgang gehabt und wie sind die Zugänge?",
        "prompt_translation": "I'm taking over the patient now. Has he had a bowel movement today and how are the IV lines?",
        "initial_prompt_audio": "icu_transfer.mp3"
    },

    # ==========================================
    # 3. DOCTORS (Professional Handovers)
    # ==========================================
    "doc_rounds": {
        "name": "📋 Doctor: Ward Rounds",
        "role": "Chief Physician",
        "difficulty": "Hard",
        "initial_prompt": "Wie sind die Vitalwerte von Frau Schmidt seit der Operation gestern? Gibt es Besonderheiten?",
        "prompt_translation": "How are Mrs. Schmidt's vitals since the surgery yesterday? Are there any particulars?",
        "initial_prompt_audio": "doc_rounds.mp3"
    },
    "doc_call": {
        "name": "📞 Doctor: Urgent Call",
        "role": "Duty Doctor (On Phone)",
        "difficulty": "Hard",
        "initial_prompt": "Hier ist Dr. Bauer. Sie haben mich angepiept. Was ist der Notfall?",
        "prompt_translation": "This is Dr. Bauer. You paged me. What is the emergency?",
        "initial_prompt_audio": "doc_call.mp3"
    },
    "doc_medication": {
        "name": "💊 Doctor: Medication Clarification",
        "role": "Junior Doctor",
        "difficulty": "Medium",
        "initial_prompt": "Ich habe Ibuprofen 800mg aufgeschrieben. Warum haben Sie das noch nicht gegeben?",
        "prompt_translation": "I prescribed Ibuprofen 800mg. Why haven't you administered it yet?",
        "initial_prompt_audio": "doc_medication.mp3"
    },

    # ==========================================
    # 4. FAMILY & FRIENDS (Empathy)
    # ==========================================
    "family_update": {
        "name": "👪 Family: Status Update",
        "role": "Worried Wife",
        "difficulty": "Medium",
        "initial_prompt": "Mein Mann liegt jetzt schon so lange im OP. Warum sagt uns niemand etwas? Ist etwas passiert?",
        "prompt_translation": "My husband has been in surgery for so long. Why is nobody telling us anything? Did something happen?",
        "initial_prompt_audio": "family_update.mp3"
    },
    "family_rules": {
        "name": "🚫 Family: Visiting Rules",
        "role": "Visitor",
        "difficulty": "Easy",
        "initial_prompt": "Ich weiß, es ist nach 20 Uhr, aber ich muss meinen Vater unbedingt noch sehen.",
        "prompt_translation": "I know it's past 8 PM, but I absolutely need to see my father.",
        "initial_prompt_audio": "family_rules.mp3"
    },
    "family_comfort": {
        "name": "😢 Family: Comforting",
        "role": "Crying Daughter",
        "difficulty": "Medium",
        "initial_prompt": "Er sieht so blass aus. Hat er Schmerzen? Wird er wieder gesund?",
        "prompt_translation": "He looks so pale. Is he in pain? Will he get healthy again?",
        "initial_prompt_audio": "family_comfort.mp3"
    },

    # ==========================================
    # 5. ADMIN & MANAGEMENT
    # ==========================================
    "admin_sick": {
        "name": "🤒 Admin: Calling in Sick",
        "role": "Head Nurse (Station Manager)",
        "difficulty": "Medium",
        "initial_prompt": "Guten Morgen. Du rufst sehr spät an. Wir sind schon unterbesetzt. Was ist los?",
        "prompt_translation": "Good morning. You are calling very late. We are already understaffed. What is going on?",
        "initial_prompt_audio": "admin_sick.mp3"
    },
    "admin_roster": {
        "name": "📅 Admin: Shift Roster",
        "role": "Roster Planner",
        "difficulty": "Easy",
        "initial_prompt": "Kannst du nächstes Wochenende den Nachtdienst für Thomas übernehmen?",
        "prompt_translation": "Can you take over the night shift for Thomas next weekend?",
        "initial_prompt_audio": "admin_roster.mp3"
    },
    "admin_docs": {
        "name": "📝 Admin: Documentation",
        "role": "Quality Manager",
        "difficulty": "Hard",
        "initial_prompt": "In der Pflegedokumentation fehlt der Eintrag zur Wundversorgung von gestern. Kannst du das erklären?",
        "prompt_translation": "The entry regarding wound care from yesterday is missing in the documentation. Can you explain that?",
        "initial_prompt_audio": "admin_docs.mp3"
    },

    # ==========================================
    # 6. SUPPORT STAFF (Interdisciplinary)
    # ==========================================
    "staff_cleaner": {
        "name": "🧹 Support: Cleaning",
        "role": "Cleaning Staff",
        "difficulty": "Easy",
        "initial_prompt": "Entschuldigung, ist das Zimmer 12 jetzt frei? Kann ich dort wischen?",
        "prompt_translation": "Excuse me, is room 12 free now? Can I mop there?",
        "initial_prompt_audio": "staff_cleaner.mp3"
    },
    "staff_physio": {
        "name": "🚶 Support: Physiotherapy",
        "role": "Physiotherapist",
        "difficulty": "Medium",
        "initial_prompt": "Ist Frau Klein heute fit genug für die Mobilisation oder ist der Kreislauf noch instabil?",
        "prompt_translation": "Is Mrs. Klein fit enough for mobilization today or is her circulation still unstable?",
        "initial_prompt_audio": "staff_physio.mp3"
    },
    "staff_kitchen": {
        "name": "🍲 Support: Dietary Needs",
        "role": "Kitchen Staff",
        "difficulty": "Easy",
        "initial_prompt": "Für Zimmer 5 steht 'Nüchtern' auf der Liste, aber der Patient fragt nach Frühstück.",
        "prompt_translation": "For room 5 it says 'Fasting' on the list, but the patient is asking for breakfast.",
        "initial_prompt_audio": "staff_kitchen.mp3"
    },

    # ==========================================
    # 7. SECURITY & SAFETY
    # ==========================================
    "security_aggressive": {
        "name": "🤬 Security: Aggressive Patient",
        "role": "Security Guard",
        "difficulty": "Hard",
        "initial_prompt": "Wir haben einen aggressiven Patienten in der Notaufnahme. Brauchen Sie Unterstützung zur Fixierung?",
        "prompt_translation": "We have an aggressive patient in the ER. Do you need support for restraint?",
        "initial_prompt_audio": "security_aggressive.mp3"
    },
    "security_theft": {
        "name": "👜 Security: Theft Report",
        "role": "Patient",
        "difficulty": "Medium",
        "initial_prompt": "Meine Geldbörse war im Nachttisch, jetzt ist sie weg! Wer war hier im Zimmer?",
        "prompt_translation": "My wallet was in the nightstand, now it's gone! Who was here in the room?",
        "initial_prompt_audio": "security_theft.mp3"
    },
    "security_access": {
        "name": "🔑 Security: Locked Door",
        "role": "New Intern",
        "difficulty": "Easy",
        "initial_prompt": "Ich habe meinen Ausweis vergessen und komme nicht in den Medikamentenraum. Können Sie mir aufschließen?",
        "prompt_translation": "I forgot my ID and can't get into the medication room. Can you unlock it for me?",
        "initial_prompt_audio": "security_access.mp3"
    },

    # ==========================================
    # 8. GENERAL PUBLIC (Lobby/Corridor)
    # ==========================================
    "public_directions": {
        "name": "🗺️ Public: Directions",
        "role": "Lost Visitor",
        "difficulty": "Easy",
        "initial_prompt": "Entschuldigung, ich suche die Kardiologie. Muss ich hier links oder rechts?",
        "prompt_translation": "Excuse me, I am looking for Cardiology. Do I have to go left or right here?",
        "initial_prompt_audio": "public_directions.mp3"
    },
    "public_parking": {
        "name": "🚗 Public: Parking",
        "role": "Visitor",
        "difficulty": "Easy",
        "initial_prompt": "Der Automat im Parkhaus nimmt mein Geld nicht. Wissen Sie, wer mir helfen kann?",
        "prompt_translation": "The machine in the parking garage isn't taking my money. Do you know who can help me?",
        "initial_prompt_audio": "public_parking.mp3"
    },
    "public_privacy": {
        "name": "🤫 Public: Privacy",
        "role": "Nosy Neighbor",
        "difficulty": "Medium",
        "initial_prompt": "Ich habe gehört, mein Nachbar, der Herr Kurz, liegt hier. Was hat er denn genau?",
        "prompt_translation": "I heard my neighbor, Mr. Kurz, is staying here. What exactly does he have?",
        "initial_prompt_audio": "public_privacy.mp3"
    }
}

def get_scenario_names():
    return [data["name"] for key, data in SCENARIOS.items()]

def get_scenario_by_name(name):
    for key, data in SCENARIOS.items():
        if data["name"] == name:
            return data
    return None

# def get_scenario_names():
#     return [data["name"] for key, data in SCENARIOS.items()]

# def get_scenario_by_name(name):
#     for key, data in SCENARIOS.items():
#         if data["name"] == name:
#             return data
#     return None