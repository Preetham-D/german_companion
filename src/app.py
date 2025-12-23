import streamlit as st
from streamlit_mic_recorder import mic_recorder
import os

# Import our modules
from scenarios import get_scenario_names, get_scenario_by_name
from audio_utils import text_to_speech_file, transcribe_audio
from llm_logic import analyze_response

# --- Page Config ---
st.set_page_config(
    page_title="German Companion AI",
    page_icon="🇩🇪",
    layout="centered"
)

# --- Custom CSS for "Cool" Look ---
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #FF4B4B;
        text-align: center;
        font-weight: 700;
    }
    .scenario-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #4F4F4F;
        margin-bottom: 20px;
    }
    .feedback-box {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #FF4B4B;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Title ---
st.markdown('<div class="main-header">🇩🇪 German AI Companion</div>', unsafe_allow_html=True)
st.write("Practice real-world scenarios with instant AI feedback.")

# --- Sidebar: Scenario Selection ---
with st.sidebar:
    st.header("⚙️ Settings")
    selected_name = st.selectbox("Choose a Scenario:", get_scenario_names())
    scenario = get_scenario_by_name(selected_name)
    
    st.divider()
    st.info(f"**Role:** {scenario['role']}\n\n**Difficulty:** {scenario['difficulty']}")

# --- Main Interaction Area ---
if scenario:
    # 1. Display Scenario Context
    # st.markdown(f"""
    # <div class="scenario-card">
    #     <h3>📍 {scenario['name']}</h3>
    #     <p style="font-size: 1.1em;">The {scenario['role']} says:</p>
    #     <h2 style="color: #4da6ff;">"{scenario['initial_prompt']}"</h2>
    # </div>
    # """, unsafe_allow_html=True)

    # 1. Display Scenario Context
    st.markdown(f"""
    <div class="scenario-card">
        <h3>📍 {scenario['name']}</h3>
        <p style="font-size: 1.1em;">The {scenario['role']} says:</p>
        <h2 style="color: #4da6ff;">"{scenario['initial_prompt']}"</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # --- NEW: Translation Expander ---
    with st.expander("👀 Need help? See English Translation"):
        st.write(f"**English:** {scenario['prompt_translation']}")
    # ---------------------------------

    # 2. Audio Prompt (Auto-generated)
    if "last_scenario" not in st.session_state or st.session_state.last_scenario != selected_name:
        audio_file = text_to_speech_file(scenario['initial_prompt'])
        st.session_state.audio_path = audio_file
        st.session_state.last_scenario = selected_name
        st.session_state.feedback = None # Reset feedback on change

    if st.session_state.get("audio_path"):
        st.audio(st.session_state.audio_path, format="audio/mp3")

    st.divider()

    # 3. Voice Input
    st.write("🎙️ **Your Turn! Reply in German:**")
    
    # This widget handles recording
    audio = mic_recorder(
        start_prompt="Start Recording",
        stop_prompt="Stop Recording",
        key='recorder',
        format="wav" # Best format for Whisper
    )

    # 4. Processing Logic
    if audio:
        with st.spinner("🎧 Listening & Analyzing..."):
            # A. Transcribe
            user_text = transcribe_audio(audio['bytes'])
            
            # B. Analyze (only if we have text)
            if user_text and "Error" not in user_text:
                feedback_data = analyze_response(user_text, scenario)
                st.session_state.feedback = feedback_data
                st.session_state.user_text = user_text
            else:
                st.error("Could not understand audio. Please try again.")

    # 5. Display Results (if available)
    if st.session_state.get("feedback"):
        data = st.session_state.feedback
        
        st.markdown("### 📊 Analysis Results")
        
        # Metrics Row
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Relevance Score", f"{data['score']}/100")
        with col2:
            st.caption("You said:")
            st.write(f"_{data['transcript_corrected']}_")

        # Feedback Cards
        with st.expander("💡 See Improvement Tips", expanded=True):
            st.markdown(f"**English Meaning:** {data['translation']}")
            st.info(f"**Tip:** {data['feedback']}")
            st.success(f"**Better Way to Say it:**\n\n_{data['better_response']}_")