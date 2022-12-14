import uvicorn
import streamlit as st
import json
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter




st.title('N-gram App')
hc_lo = st.selectbox('Which HC would you like to select the N-gram for?', ('#algorithms', '#confidenceintervals',
                                                                           '#correlation', '#deduction',
                                                                           '#descriptivestats', '#distributions',
                                                                           '#modeling', '#probability', '#regression',
                                                                           '#significance'))

st.write('')
st.write("Select the grade and the N-gram size from slider below")
grade = st.slider('Select a value for grade', 1, 5, 3)
n = st.slider('Select a value for N-gram size', 1, 4, 3)

inputs = {'hc_lo': hc_lo, 'grade': grade, 'n': n}


poll_response = st.text_area('Enter a poll response here')
poll_hclo = st.selectbox('Select a value for the HC to be graded on', ('#algorithms', '#confidenceintervals',
                                                                           '#correlation', '#deduction',
                                                                           '#descriptivestats', '#distributions',
                                                                           '#modeling', '#probability', '#regression',
                                                                           '#significance'))

grading = {'poll_response': poll_response, 'poll_hclo': poll_hclo}


if st.button('N-gramize'):
    res = requests.post(url='http://127.0.0.1:8000/ngram', data=json.dumps(inputs))
    print(res.text)
    st.subheader(f'Response from API = {res.text}')

if st.button('Grade'):
    res = requests.post(url='http://127.0.0.1:8000/feedback', data=json.dumps(grading))
    res_js = res.json()
    print(res_js)
    print('')
    print(res)

    st.subheader(f'The following components were missing from the response:')

    # if first char is letter, display it

    if res_js[0][0].isalpha():
        st.write(f'1. {res_js[0]}')
    else:
        st.write(f'1. {res_js[0][1].upper() + res_js[0][2:]}')

    for i in range(1, len(res_js)):
        # sentence case the phrase
        st.write(f'{i+1}. {res_js[i][1].upper() + res_js[i][2:]}.')


