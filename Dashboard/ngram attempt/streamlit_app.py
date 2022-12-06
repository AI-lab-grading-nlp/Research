import streamlit as st

def main_page():
    st.markdown("# Main page")
    st.sidebar.markdown("# Main page")

def page2():
    st.markdown("# N-Grams")
    st.sidebar.markdown("# N-grams")

page_names_to_funcs = {
    "Main Page": main_page,
    "N-grams": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

import uvicorn
import streamlit as st
import json
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter




st.title('Poll Feedback App')


poll_response = st.text_area('Enter a poll response here')
poll_hclo = st.selectbox('Select a value for the HC to be graded on', ('#algorithms', '#confidenceintervals',
                                                                           '#correlation', '#deduction',
                                                                           '#descriptivestats', '#distributions',
                                                                           '#modeling', '#probability', '#regression',
                                                                           '#significance'))

grading = {'poll_response': poll_response, 'poll_hclo': poll_hclo}


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


