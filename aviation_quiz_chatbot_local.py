"""
Aviation Quiz Chatbot using Streamlit
"""
import streamlit as st

# In-memory quiz database
QUIZ_QUESTIONS = [
    {
        "question": "What is the minimum safe altitude over a congested area?",
        "options": [
            "A. 500 feet above the highest obstacle",
            "B. 1,000 feet above the highest obstacle within a horizontal radius of 2,000 feet",
            "C. 2,000 feet above ground level",
            "D. 500 feet above ground level"
        ],
        "answer": "B"
    },
    {
        "question": "What does a flashing red light from the control tower mean to an aircraft on the ground?",
        "options": [
            "A. Cleared to taxi",
            "B. Stop",
            "C. Taxi clear of runway in use",
            "D. Return to starting point on airport"
        ],
        "answer": "C"
    },
    {
        "question": "What is the primary purpose of the rudder on an aircraft?",
        "options": [
            "A. To control pitch",
            "B. To control yaw",
            "C. To control roll",
            "D. To increase lift"
        ],
        "answer": "B"
    },
    {
        "question": "Which instrument indicates whether the aircraft is climbing, descending, or in level flight?",
        "options": [
            "A. Altimeter",
            "B. Airspeed Indicator",
            "C. Vertical Speed Indicator",
            "D. Heading Indicator"
        ],
        "answer": "C"
    },
    {
        "question": "What is the standard direction of turns in a holding pattern?",
        "options": [
            "A. Left",
            "B. Right",
            "C. Either direction",
            "D. Depends on ATC instructions"
        ],
        "answer": "B"
    }
]

def get_next_question(idx):
    if idx < len(QUIZ_QUESTIONS):
        return QUIZ_QUESTIONS[idx]
    return None

st.title("Aviation Quiz Chatbot ✈️")

if "quiz_idx" not in st.session_state:
    st.session_state.quiz_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_result" not in st.session_state:
    st.session_state.show_result = False

question = get_next_question(st.session_state.quiz_idx)

if question and not st.session_state.show_result:
    st.subheader(f"Question {st.session_state.quiz_idx + 1}")
    st.write(question["question"])
    user_answer = st.radio("Choose your answer:", question["options"])
    if st.button("Submit"):
        correct_option = [opt for opt in question["options"] if opt.startswith(question["answer"] + ".")][0]
        if user_answer == correct_option:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. The correct answer is: {correct_option}")
        st.session_state.quiz_idx += 1
        if st.session_state.quiz_idx >= len(QUIZ_QUESTIONS):
            st.session_state.show_result = True
        st.rerun()
elif st.session_state.show_result:
    st.subheader("Quiz Complete!")
    st.write(f"Your score: {st.session_state.score} / {len(QUIZ_QUESTIONS)}")
    if st.button("Restart Quiz"):
        st.session_state.quiz_idx = 0
        st.session_state.score = 0
        st.session_state.show_result = False
        st.rerun()
else:
    st.write("No more questions.")
