from fastapi import FastAPI
from pydantic import BaseModel
import json
from comp_checker import process_most_likely
from typing import List


class UserInput4(BaseModel):
    poll_response_1: str
    poll_hc_lo_1: str



app = FastAPI()


@app.post('/mostlikelyhere')
def process(input: UserInput4):
    result = list(process_most_likely(input.poll_response_1, input.poll_hc_lo_1))
    return result

