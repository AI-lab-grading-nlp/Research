from collections import defaultdict
from random import randint

import streamlit as st
from annotated_text import annotated_text, annotation
import json
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import re




st.title('Most likely here')


poll_response_1 = st.text_area('Enter a poll response here')
poll_hc_lo_1 = st.selectbox('Which HC would you like to compare the poll response to?', ('#algorithms', '#confidenceintervals',
                                                                           '#correlation', '#deduction',
                                                                           '#descriptivestats', '#distributions',
                                                                           '#modeling', '#probability', '#regression',
                                                                           '#significance'))
new_string = " ".join(poll_response_1.splitlines())

inputs_1 = {'poll_response_1': new_string, 'poll_hc_lo_1': poll_hc_lo_1}


if st.button('Find most likely'):
    data = json.dumps(inputs_1)
    result = requests.post(url='http://127.0.0.1:8000/mostlikelyhere', data=json.dumps(inputs_1))
    result_json = result.json()

    st.subheader(f'The rubric components were most obviously present here:')

    # get the top 3 sent similarities for each component
    components = defaultdict(tuple)
    for i in range(len(result_json)):
        if result_json[i][0][0] not in components:
            components[result_json[i][0][0]] = ('', float('-inf'), [])

    # Refactor the format into "{component : (sent, sim, span)}"
    for i in range(len(result_json)):
        # Parse through the result_json and find the highest similarity for each component
        if result_json[i][1][0] > components[result_json[i][0][0]][1]:
            components[result_json[i][0][0]] = (result_json[i][0][1], result_json[i][1][0], [result_json[i][1][1]])
 

    # go through response and highlight the matching span for each component
    with st.spinner('Highlighting...'):
        used = set()
        for comp, (sent, sim, span) in components.items():
            annot = str(comp) + ' ' + 'with document similarity of' + ' ' + str(round(sim, 2))
            span_start = span[0][0]
            span_end = span[0][1]

            # list of pastel or neon highlight colors
            pastels = ['#93f4e8', '#fecf89', '#88d8ff', '#ff88b1', '#9ff88f', '#ffa088', '#efdff9', '#fd7c6e']
            
            # get random pastel color
            color = pastels[randint(0, len(pastels) - 1)]
            while color in used:
                color = pastels[randint(0, len(pastels) - 1)]
            used.add(color)
            
            if len(span) > 0:
                annotated_text(
                    poll_response_1[0:span_start], (poll_response_1[span_start+1:span_end], annot, color), poll_response_1[span_end:]
                )
                st.write('')
            else:
                st.write(f'{comp} was not found in the sentence')



    with st.expander('Show detailed results:'):
        st.write('The following are the rubric components matched to the sentence and the similarity score:')
        for i in range(len(result_json)):
            comp = result_json[i][0][0]
            sent = result_json[i][0][1]
            sim = result_json[i][1][0]
            span = result_json[i][1][1]
            st.write(f'Component: {comp}')
            st.write(f'Sentence: {sent}')
            st.write(f'Similarity: {sim}')
            st.write(f'Span: {span}')
            st.write('')


