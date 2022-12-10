from fastapi import FastAPI
from pydantic import BaseModel
from ngram import ngramize
import json
from comp_checker import get_feedback, process_most_likely
from typing import List
from bloom_questions import infer, create_prompt

class UserInput(BaseModel):
    hc_lo: str
    grade: int
    n: int


class UserInput3(BaseModel):
    poll_response: str
    poll_hclo: str


class UserInput4(BaseModel):
    poll_response_1: str
    poll_hc_lo_1: str

class UserInput5(BaseModel):
    answers: str
    


app = FastAPI()

@app.post('/ngram')
def operate(input:UserInput):
    print('Hello world')
    result = ngramize(input.hc_lo, input.grade, input.n)
    return result

@app.post('/feedback')
def feedback(input:UserInput3):
    print('Hello world')
    result = get_feedback(input.poll_response, input.poll_hclo)
    return result

@app.post('/mostlikelyhere')
def process(input: UserInput4):
    result = list(process_most_likely(input.poll_response_1, input.poll_hc_lo_1))
    print(type(result), 'TYPE YOU ARE MY TYPE')
    return result

@app.post('/questioncreation')
def question_creation(input: UserInput5):
    
    prompt = create_prompt(input.answers)    
    res = infer(prompt)
    print(res)
    if res['error']:
        return res['error']
    return res[0]['generated_text']
    


# # For running streamlit app
# streamlit run stream_lit.py
# # For running backend with FastAPI
# uvicorn fast_api:app --reload

