import streamlit as st
import random

st.set_page_config(page_title="NUMBER GUESSING", page_icon="🎲", layout="centered")

# 🎨 Dark theme styling
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #f0f0f0;
        min-height: 100vh;
        background-attachment: fixed;
    }
    .main-title {
        font-size: 2.5em;
        font-weight: 800;
        color: #f0f0f0;
        margin-bottom: 0.2em;
        text-align: center;
    }
    .subtitle {
        font-size: 1.2em;
        color: #dddddd;
        margin-bottom: 1.5em;
        text-align: center;
    }
    .diff-btn {
        padding: 0.6em 1.8em;
        border-radius: 1.5em;
        border: 2px solid #ffffff;
        background-color: #ffffff;
        color: #000000;
        font-size: 1.1em;
        font-weight: 600;
        margin: 0 0.4em 0.7em 0.4em;
        transition: all 0.3s ease;
    }
    .diff-btn-selected {
        background-color: #3777f0;
        color: #ffffff;
        font-weight: 700;
        border: 2px solid #3777f0;
    }
    </style>
""", unsafe_allow_html=True)

# 🎲 Game title and intro
st.markdown('<div class="main-title"> 🎭NUMBER GUESSING </div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Guess the number between <b>1</b> and <b>100</b>. Choose a level and start guessing!</div>', unsafe_allow_html=True)

# 🔁 Session state setup
if "difficulty" not in st.session_state:
    st.session_state.difficulty = None
if "max_attempts" not in st.session_state:
    st.session_state.max_attempts = 10
if "secret_number" not in st.session_state:
    st.session_state.secret_number = None
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_active" not in st.session_state:
    st.session_state.game_active = False
if "message" not in st.session_state:
    st.session_state.message = ""

# 🎮 Difficulty buttons
# diffs = [("Easy", 10), ("Medium", 7), ("Hard", 5)]
# diff_cols = st.columns(len(diffs))
# for i, (label, attempts) in enumerate(diffs):
#     btn_class = "diff-btn diff-btn-selected" if st.session_state.difficulty == label else "diff-btn"
#     if diff_cols[i].button(f"🎯 {label}", key=label, help=f"{attempts} attempts", use_container_width=True):
#         st.session_state.difficulty = label
#         st.session_state.max_attempts = attempts
#         st.session_state.secret_number = None
#         st.session_state.attempts = 0
#         st.session_state.game_active = False
#         st.session_state.message = ""

# New: One-column vertical layout
diffs = [("Easy", 10), ("Medium", 7), ("Hard", 5)]
for label, attempts in diffs:
    button_label = f"🎯 {label}"
    if st.button(button_label, key=label):
        st.session_state.difficulty = label
        st.session_state.max_attempts = attempts
        st.session_state.secret_number = None
        st.session_state.attempts = 0
        st.session_state.game_active = False
        st.session_state.message = ""


# 🟢 Start game
if st.session_state.difficulty and not st.session_state.game_active:
    st.markdown(f"**🎮 Difficulty Selected:** `{st.session_state.difficulty}` with **{st.session_state.max_attempts} attempts**")
    if st.button("Start Game"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_active = True
        st.session_state.message = ""

# 🔢 Main game logic
if st.session_state.game_active:
    st.markdown(f"**🧮 Attempts Left:** `{st.session_state.max_attempts - st.session_state.attempts}`")
    guess = st.number_input("🔢 Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")
    if st.button("Guess"):
        st.session_state.attempts += 1
        if guess == st.session_state.secret_number:
            st.success(f"🎉 Correct! You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.game_active = False
        elif st.session_state.attempts >= st.session_state.max_attempts:
            st.error(f"❌ Game Over! The number was `{st.session_state.secret_number}`.")
            st.session_state.game_active = False
        elif guess < st.session_state.secret_number:
            st.info("📉 Too low. Try a higher number.")
        else:
            st.info("📈 Too high. Try a lower number.")

# 🔁 Play Again
if st.session_state.difficulty and not st.session_state.game_active and st.session_state.secret_number is not None:
    if st.button("🔄 Play Again"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_active = True
        st.session_state.message = ""
