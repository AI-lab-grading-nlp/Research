import pandas as pd
import json
import numpy as np

import spacy

nlp = spacy.load('en_core_web_lg')


data = pd.read_csv('mu_responses.csv')
data.head()

data = data.rename(columns={
    'Polls ID': 'poll_id',
    'Assessment reports Student ID': 'student_id',
    'Poll Responses Response':'response',
    'Assessment reports Hashtag':'HC',
    'Assessment reports Score':'score'})
data.head()


hclo_lst = ['#algorithms', '#confidenceintervals','#correlation', '#deduction', '#descriptivestats', '#distributions',
                                                    '#modeling', '#probability', '#regression', '#significance']

hclos_dfs = {}
for hclo in hclo_lst:
    hclos_dfs[hclo] = data.loc[data['HC'] == hclo]


with open('rubrics.txt') as f:
    data = f.read()
js = json.loads(data)


def doc_sim_check_rubric(response, hclo, threshold=0.85):
    rel_rubric = js[hclo]
    comp_present = np.zeros(len(rel_rubric))

    doc2 = nlp(response)

    for i in range(len(rel_rubric)):
        doc1 = nlp(rel_rubric[i])
        comp_present[i] = doc1.similarity(doc2)
        # needs to be trained
        sim = doc1.similarity(doc2)
        if sim > threshold:
            comp_present[i] = 1
        else:
            comp_present[i] = 0
        print(rel_rubric[i])
        print(sim)
        print(comp_present)

    return comp_present


# given components, return feedback for which were missing
def get_missing(components, hclo):
    rel_rubric = js[hclo]
    missing = []
    for i in range(len(components)):
        if components[i] == 0:
            missing.append(rel_rubric[i])
    return missing


def get_feedback(response, HC):
    threshold = 0.85
    components = doc_sim_check_rubric(response, HC)
    missing = get_missing(components, HC)
    if missing == []:
        missing = ['Nothing missing!']
    return missing

ans = get_feedback(hclos_dfs['#algorithms']['response'].iloc[2], '#algorithms')
print(ans, type(ans))