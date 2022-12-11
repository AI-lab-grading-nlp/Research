import streamlit as st
import json
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
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




st.title('Question Creation with Davinci')



answers = st.text_area('Enter your answers here separated by ";-"', '1;-\n2')

st.write('')



inputs = {'answers': answers}

def create_prompt(answers):

    prompt = ''''''
    answers = answers.split(';-')
    for i, answer in enumerate(answers):
        prompt += f'''Prompt {i+1}: {answer}\n'''
    fin = '''Question: What question are all the prompts above answering? \n Answer(in the form of a question): '''
    
    prompt += fin
    

    return prompt


if st.button('Create Question'):
    # print('The inputs are',inputs)
    # res = requests.post(url='http://127.0.0.1:8000/questioncreation', data=json.dumps(inputs))
    
    prompt = create_prompt(answers)
    
    st.subheader(f'The following was the question created:')

    answer = get_response(prompt)
    
    st.write(answer)


