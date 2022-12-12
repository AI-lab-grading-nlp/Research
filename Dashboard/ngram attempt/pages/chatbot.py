import streamlit as st
from streamlit_chat import message as st_message

import os
import openai
from dotenv import load_dotenv
from io import StringIO

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG")


def get_response(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    return response.choices[0].text




if "history" not in st.session_state:
    st.session_state.history = []

st.title("Hello Chatbot")



uploaded_file = st.file_uploader("Choose a file")


import random
for chat in st.session_state.history:
    st_message(**chat, key=random.randint(0, 1000000))
    
def generate_answer():
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()

    
    user_message = st.session_state.input_text
    if user_message == "":
        return
    
    if string_data is not None:
        session_history_text = 'Prompt: ' + string_data
        session_history_text += f" \nMarvin is a chatbot that aids in understanding any topic and tests your knowledge by letting you respond to his questions. \n\n"
        session_history_text += f"You: {user_message}\nMarvin: "
    else:
        session_history_text = f" \nMarvin is a chatbot that aids in understanding any topic and tests your knowledge. \n\n"
    
    for chat in st.session_state.history:
        if chat["is_user"]:
            session_history_text += f"You: {chat['message']}"
        else:
            session_history_text += f"Marvin: {chat['message']}"
    
    session_history_text += f"You: {user_message}\nMarvin: "

    result = get_response(session_history_text)

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": result, "is_user": False})
    
st.text_input("Talk to the bot", key="input_text",  on_change=generate_answer)