import streamlit as st
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Custom CSS for Enhanced UI
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #1E3C72, #2A5298);
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    .stApp {
        background-color: transparent;
    }
    .stButton>button {
        background-color: #FFD700;
        color: black;
        font-weight: bold;
        border-radius: 12px;
        padding: 14px 28px;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #FFC107;
    }
    .card {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
    }
    .stHeader {
        color: #FFD700;
        font-size: 26px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title 
st.title("🚀 Growth Mindset Challenge")
st.write("\n")
st.markdown("<div class='card'><h3 style='text-align:center;'>Unlock your potential with this interactive challenge!</h3></div>", unsafe_allow_html=True)

# Personalized Greeting with Typing Effect
user_name = st.text_input("Enter your name:")
if user_name:
    with st.spinner("Loading..."):
        time.sleep(1)
    st.success(f"Welcome, **{user_name}**! Let's grow together. 🌱")

# Quiz Section 
st.header("📝 Growth Mindset Quiz")
st.markdown("<div class='card'>", unsafe_allow_html=True)
questions = [
    "I believe my intelligence can improve with effort.",
    "I enjoy challenges and learn from them.",
    "I see mistakes as opportunities to grow.",
    "I persist even when tasks are difficult.",
    "I value feedback and use it to improve."
]
responses = []
progress_val = 0
for i, question in enumerate(questions):
    response = st.radio(question, ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key=i)
    responses.append(response)
    progress_val += 20  # Increment progress per question
    st.progress(progress_val / 100)
st.markdown("</div>", unsafe_allow_html=True)

# Score Calculation
if st.button("Submit Quiz"):
    score = sum([5 if r == "Strongly Agree" else 4 if r == "Agree" else 3 if r == "Neutral" else 2 if r == "Disagree" else 1 for r in responses])
    with st.spinner("Calculating your mindset score..."):
        time.sleep(2)
    st.subheader("🎯 Your Growth Mindset Score:")
    st.write(f"**{score}/25**")
    if score > 20:
        st.balloons()
    fig, ax = plt.subplots()
    ax.pie([score, 25 - score], labels=["Growth Mindset", "Remaining"], colors=["#FFD700", "#444444"], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Daily Growth Challenge 
st.header("💡 Daily Growth Challenge")
st.markdown("<div class='card'>", unsafe_allow_html=True)
challenges = [
    "Read 5 pages of a book 📖",
    "Learn a new word and use it in a sentence 📝",
    "Take a 10-minute mindful break ☕",
    "Write down one thing you're grateful for 🙏",
    "Try a new skill for 15 minutes 🎨"
]
st.write(f"**Today's Challenge:** {random.choice(challenges)}")
st.markdown("</div>", unsafe_allow_html=True)

# Gamification: Points & Badges
st.header("🏆 Gamification")
st.markdown("<div class='card'>", unsafe_allow_html=True)
points = st.session_state.get("points", 0)
if st.button("Complete Challenge"):
    points += 10
    st.session_state.points = points
    st.success(f"🎉 You earned 10 points! Total Points: {points}")
    if points >= 50:
        st.snow()
        st.success("🎖️ Congrats! You unlocked the **Growth Master** Badge!")
st.markdown("</div>", unsafe_allow_html=True)

# Inspirational Quotes 
st.header("📜 Inspirational Quotes")
st.markdown("<div class='card'>", unsafe_allow_html=True)
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "You don’t have to be great to start, but you have to start to be great. – Zig Ziglar"
]
selected_quote = st.selectbox("Choose a quote:", quotes)
st.write(f"*{selected_quote}*")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("Made with ❤️ by Muhammad Moeed")
