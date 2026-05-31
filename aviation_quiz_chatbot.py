"""
Aviation Quiz Chatbot using Streamlit and OpenAI
"""
import streamlit as st
import openai
import os

# Set your OpenAI API key here or use an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "your-openai-api-key")

st.title("Aviation Quiz Chatbot ✈️")
st.write("Ask me any aviation quiz question or let me quiz you!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    prompt = "You are an expert aviation quiz chatbot. Answer the user's aviation quiz question or ask a new aviation quiz question. If the user wants to be quizzed, ask a multiple-choice question and wait for their answer. If they answer, tell them if they are correct and explain the answer.\n" + "\n".join([f"{role}: {msg}" for role, msg in st.session_state.chat_history])
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        bot_reply = response.choices[0].message.content.strip()
    except Exception as e:
        bot_reply = f"Error: {e}"
    st.session_state.chat_history.append(("Bot", bot_reply))

for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Bot:** {msg}")

st.info("Note: Set your OpenAI API key in the environment variable OPENAI_API_KEY or replace 'your-openai-api-key' in the code.")
