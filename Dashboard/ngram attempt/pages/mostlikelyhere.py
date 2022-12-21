from collections import defaultdict
from random import randint

import streamlit as st
from annotated_text import annotated_text, annotation
import json
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter




st.title('Most likely here')


poll_response_1 = st.text_area('Enter a poll response here')
poll_hc_lo_1 = st.selectbox('Which HC would you like to compare the poll response to?', ('#algorithms', '#confidenceintervals',
                                                                           '#correlation', '#deduction',
                                                                           '#descriptivestats', '#distributions',
                                                                           '#modeling', '#probability', '#regression',
                                                                           '#significance'))
import re
new_string = " ".join(poll_response_1.splitlines())

inputs_1 = {'poll_response_1': new_string, 'poll_hc_lo_1': poll_hc_lo_1}


if st.button('Find most likely'):
    data = json.dumps(inputs_1)
    res = requests.post(url='http://127.0.0.1:8000/mostlikelyhere', data=json.dumps(inputs_1))
    res_js = res.json()

    st.subheader(f'The rubric components were most obviously present here:')
    print(res_js)

    # get the top 3 sent similarities for each component
    comps = defaultdict(tuple)
    for i in range(len(res_js)):
        if res_js[i][0][0] not in comps:
            comps[res_js[i][0][0]] = ('', float('-inf'), [])

    # comp : (sent, sim, span)
    for i in range(len(res_js)):
        if res_js[i][1][0] > comps[res_js[i][0][0]][1]:
            comps[res_js[i][0][0]] = (res_js[i][0][1], res_js[i][1][0], [res_js[i][1][1]], res_js[i][1][2], res_js[i][1][3])
 

    # go through response and highlight the matching span for each component


    print(poll_response_1)
    with st.spinner('Highlighting...'):
        used = set()
        for comp, (sent, sim, span, old, new) in comps.items():
            print(comp, sent, sim, span)
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
        for i in range(len(res_js)):
            comp = res_js[i][0][0]
            sent = res_js[i][0][1]
            sim = res_js[i][1][0]
            span = res_js[i][1][1]
            st.write(f'Component: {comp}')
            st.write(f'Sentence: {sent}')
            st.write(f'Similarity: {sim}')
            st.write(f'Span: {span}')
            st.write('')


    # match component to the sentence with the highest similarity, highlight that sentence

    # get unique components
    # comps = [i[0][0] for i in res_js]
    # for i in range(len(res_js)):
    #     print(res_js[i][0][0])
    #
    # comps = []
    # for comp in comps:
    #     max_sim = 0
    #     max_sent = ''
    #     for i in range(len(res_js)):
    #         if res_js[i][0][0] == comp:
    #             if res_js[i][1][0] > max_sim:
    #                 max_sim = res_js[i][1][0]
    #                 max_sent = res_js[i][0][1]
    #     st.write(f'Component: {comp}')
    #     st.write(f'Sentence: {max_sent}')
    #     st.write(f'Similarity: {max_sim}')
    #     st.write('')


    # Write the response and highlight the parts that were present in the sentence
