import streamlit as st
import json
import requests

st.title('Basic Calculator App')
option = st.selectbox('What operation would you like to perform?', ('add', 'subtract', 'multiply', 'divide'))

st.write('')
st.write("Select the numbers from slider below")
x = st.slider('Select a value for x', 0, 100, 50)
y = st.slider('Select a value for y', 0, 100, 50)

inputs = {'operation': option, 'x': x, 'y': y}

if st.button('Calculate'):
    res = requests.post(url = 'http://127.0.0.1:8000/calculate', data=json.dumps(inputs))
    st.subheader(f'Response from API = {res.text}')