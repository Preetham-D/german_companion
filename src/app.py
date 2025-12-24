import streamlit as st
import os
import shutil
from audio_utils import text_to_speech_file, transcribe_audio
from llm_logic import analyze_response
from scenarios import SCENARIOS, get_scenario_names, get_scenario_by_name

# --- PAGE CONFIG ---
st.set_page_config(page_title="BorderPlus Nurse Trainer", page_icon="🏥")

# --- CSS STYLING (Fixed for Dark Mode) ---
st.markdown("""
    <style>
    /* Force text color to black for these specific light-colored cards */
    .scenario-card {
        background-color: #f0f2f6;
        color: #000000 !important;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 20px;
    }
    .scenario-card h2, .scenario-card h3, .scenario-card p {
        color: #000000 !important;
    }

    .user-card {
        background-color: #e8f5e9;
        color: #000000 !important;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }
    .user-card h4, .user-card p, .user-card i {
        color: #000000 !important;
    }

    .feedback-card {
        background-color: #e3f2fd;
        color: #000000 !important;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }
    .feedback-card h4, .feedback-card p, .feedback-card b {
        color: #000000 !important;
    }
    
    /* Ensure the score is visible */
    .score-text {
        font-weight: bold;
        font-size: 2em;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("🏥 Nurse Scenarios")
selected_name = st.sidebar.selectbox("Choose a Situation:", get_scenario_names())
scenario = get_scenario_by_name(selected_name)

# --- MAIN TITLE ---
st.title("🇩🇪 BorderPlus AI Companion")
st.caption("Medical German Simulator for International Nurses")

if scenario:
    # 1. Display Scenario Context
    st.markdown(f"""
    <div class="scenario-card">
        <h3>📍 {scenario['name']}</h3>
        <p style="font-size: 1.1em;">The {scenario['role']} says:</p>
        <h2 style="color: #4da6ff !important;">"{scenario['initial_prompt']}"</h2>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("👀 Need help? See English Translation"):
        st.write(f"**English:** {scenario['prompt_translation']}")

    # 2. Play Audio Prompt
    if "initial_prompt_audio" in scenario:
        audio_file = scenario["initial_prompt_audio"]
        # If file doesn't exist locally, generate it on the fly
        if not os.path.exists(audio_file):
            temp_path = text_to_speech_file(scenario['initial_prompt'])
            if temp_path and os.path.exists(temp_path):
                shutil.move(temp_path, audio_file)
        
        # Display audio player if file exists
        if os.path.exists(audio_file):
            st.audio(audio_file)

    # 3. Audio Recorder
    st.markdown("### 🎙️ Your Response")
    audio_value = st.audio_input("Record your answer in German")

    # 4. Process Input
    if audio_value:
        st.info("Transcribing and Analyzing...")
        
        # Transcribe
        audio_bytes = audio_value.read()
        user_text = transcribe_audio(audio_bytes)
        
        # Analyze
        feedback_data = analyze_response(user_text, scenario)
        st.session_state.feedback = feedback_data # Save to session
        
    # 5. Display Results
    if st.session_state.get("feedback"):
        data = st.session_state.feedback
        
        # Error handling display
        if "error" in data:
             st.error(f"⚠️ Error details: {data['error']}")

        st.markdown("### 📊 Analysis Results")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="user-card">
                <h4>Your Speech</h4>
                <p>🇩🇪 {data['transcript_corrected']}</p>
                <p><i>🇺🇸 {data['translation']}</i></p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            score_val = data.get('score', 0)
            score_color = "green" if isinstance(score_val, int) and score_val > 70 else "orange"
            
            st.markdown(f"""
            <div class="feedback-card">
                <h4>Relevance Score</h4>
                <div class="score-text" style="color:{score_color};">{score_val}/100</div>
                <p><b>Tip:</b> {data['feedback']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # --- Better Response Section ---
        st.subheader("💡 A Better Way to Say It")
        
        st.success(f"🇩🇪 **German:** {data['better_response']}")
        st.info(f"🇺🇸 **English:** {data.get('better_response_translation', '-')}")
        
        # Generate TTS for the better response on the fly
        if data['better_response'] != "-" and data['better_response'] != None:
            with st.spinner("Generating audio for best response..."):
                # We reuse the same function
                best_audio_path = text_to_speech_file(data['better_response'])
                if best_audio_path:
                    st.audio(best_audio_path, format="audio/mp3")