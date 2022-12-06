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


if st.button('N-gramize'):
    res = requests.post(url='http://127.0.0.1:8000/ngram', data=json.dumps(inputs))
    print(res.text)
    res_js = res.json()

    st.subheader(f'The following were the n-grams and their counts:')
    for i in range(len(res_js)):
        st.write(f'{res_js[i][0]}: {res_js[i][1]}')

