from fastapi import FastAPI
from pydantic import BaseModel
from ngram import ngramize
import json
from comp_checker import get_feedback

class UserInput(BaseModel):
    hc_lo: str
    grade: int
    n: int

class UserInput2(BaseModel):
    crap: str

class UserInput3(BaseModel):
    poll_response: str
    poll_hclo: str


app = FastAPI()

@app.post('/ngram')
def operate(input:UserInput):
    print('Hello world')
    result = ngramize(input.hc_lo, input.grade, input.n)
    return result


@app.post('/try')
def work(input:UserInput2):
    result = 'crap'
    print('crap')
    return result

@app.post('/feedback')
def feedback(input:UserInput3):
    print('Hello world')
    result = get_feedback(input.poll_response, input.poll_hclo)
    return result


# # For running streamlit app
# streamlit run stream_lit.py
# # For running backend with FastAPI
# uvicorn fast_api:app --reload