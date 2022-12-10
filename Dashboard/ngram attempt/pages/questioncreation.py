import streamlit as st
import json
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter




st.title('Question Creation with Bloom')



answers = st.text_area('Enter your answers here in separate lines', '1\n2')

st.write('')



inputs = {'answers': answers}



if st.button('Create Question'):
    print('The inputs are',inputs)
    res = requests.post(url='http://127.0.0.1:8000/questioncreation', data=json.dumps(inputs))
    
    st.subheader(f'The following was the question created:')

    res = res.json()
    st.write(res)

