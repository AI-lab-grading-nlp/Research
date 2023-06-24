from collections import defaultdict

import pandas as pd
import json
import numpy as np
from rubrics import rubrics_dict
import spacy
from hclos_responses_dict import hclos_responses
import re


nlp = spacy.load('en_core_web_lg')

# Load data of previous student responses
data = pd.read_csv('mu_responses.csv')
data.head()
data = data.rename(columns={
    'Polls ID': 'poll_id',
    'Assessment reports Student ID': 'student_id',
    'Poll Responses Response':'response',
    'Assessment reports Hashtag':'HC',
    'Assessment reports Score':'score'})


# Split data into a dictionary of dataframes for each HC
hclo_lst = ['#algorithms', '#confidenceintervals','#correlation', '#deduction', '#descriptivestats', '#distributions',
                                                    '#modeling', '#probability', '#regression', '#significance']
hclos_dfs = {}
for hclo in hclo_lst:
    hclos_dfs[hclo] = data.loc[data['HC'] == hclo]


class HC:
    def __init__(self, name):
        self.name = name
        self.rubric = rubrics_dict[name]
        self.exemplary_answers = hclos_responses[f'{name}_4']


class Response:

    def __init__(self, response, hc):
        self.response = response
        self.hc = hc
        self.sentences_fragments = self.break_into_sentences()
        self.similarity_to_exemplary = self.get_similarity_to_exemplary()
        self.dictionary_of_sentences = {}

    def break_into_sentences(self):
        return re.split('[-:;,.!?]', self.response)

    def find_span(self, sentence):
        """Find the span (start and end indicices) of the sentence in the response."""
        return re.search(sentence, self.response, re.IGNORECASE).span()

    def get_similarity(self, response, other_response):
        return nlp(self.response).similarity(nlp(other_response))

    def get_similarity_to_exemplary(self):
        """Return the average similarity of the response to the exemplary answers."""
        sim_to_exemplary = 0
        
        for prev_resp in self.hc.exemplary_answers:
            sim_to_exemplary += self.get_similarity(self.response, prev_resp)
        sim_to_exemplary /= (len(self.hc.exemplary_answers) + 1)
        
        return sim_to_exemplary
    

    def get_similarity_to_rubric(self):
        """Return a dictionary of the similarity of each sentence/fragment to each rubric component as well as the span of that sentence/fragment."""
        for sent in self.sentences_fragments:
            for rubric_component in self.hc.rubric:
                sim_to_rubric = self.get_similarity(sent, rubric_component)
                span = self.find_span(sent)
                self.dictionary_of_sentences[(rubric_component, sent)] = (sim_to_rubric, span)

        return self.dictionary_of_sentences




def process_most_likely(response, hc):
    """
    inputs:
        response: string of student response
        HC: string of HC to be graded on
    outputs:
        lst: a list of tuples in the following format:
            ((rubric component, sentence/fragment), 
                similarity to rubric, span of sentence in response).
    """
    
    current_response = Response(response, HC(hc))
    comp_sentence_dict = current_response.get_similarity_to_rubric()

    lst = []
    # order the comp_sentence_dict first by component, then by similarity to rubric
    comp_sentence_dict = sorted(comp_sentence_dict.items(), key=lambda x: (x[0][0], x[1][0]), reverse=True)
    
    # in list format because of some issues with json.dumps
    for i in comp_sentence_dict:
        lst.append(i)
    return lst