import pandas as pd
import nltk
import gensim
import json
#
# df = pd.read_csv('mu_responses.csv')
# df['Poll Responses Response'] = df['Poll Responses Response'].dropna().astype('string').apply(
#     lambda x: gensim.utils.simple_preprocess(x))
# # hclo_lst = df['Assessment reports Hashtag'].dropna().unique().tolist()
#
# hclo_lst = ['#algorithms', '#confidenceintervals','#correlation', '#deduction', '#descriptivestats', '#distributions',
#                                                     '#modeling', '#probability', '#regression', '#significance']
#
# # Make a dataframe for each HC/LO
# hclos_dfs = {}
# for hclo in hclo_lst:
#     hclos_dfs[hclo] = df.loc[df['Assessment reports Hashtag'] == hclo]
#
# # Make dataframes for each score of each HC/LO
# hclos_scores_dfs = {}
#
# import itertools
#
# for hclo in hclo_lst:
#     cur_df = hclos_dfs[hclo]
#     for grade in range(1, 6):
#         hclos_scores_dfs[f'{hclo}_{grade}'] = cur_df.loc[cur_df['Assessment reports Score'] == grade]['Poll Responses Response'].to_list()
#
#         hclos_scores_dfs[f'{hclo}_{grade}'] = list(itertools.chain( *hclos_scores_dfs[f'{hclo}_{grade}']))
#
#
# import json
#
# details = hclos_scores_dfs
# with open('hclos_scores_dfs.txt', 'w') as convert_file:
#     convert_file.write(json.dumps(details))
#
# print('converted')
#

hclos_scores_dfs = {}
with open('hclos_scores_dfs.txt') as f:
    data = f.read()

js = json.loads(data)
# print(js['#algorithms_1'])


def ngramize(hc_lo, grade, n):
    """Return n-gram of hc_lo and grade."""
    ngrams = pd.Series(nltk.ngrams(js[f'{hc_lo}_{grade}'], n)).value_counts()[:10]
    ngrams = ngrams.to_frame().reset_index()
    words = [' '.join(ngram) for ngram in ngrams['index'].to_list()]
    counts = ngrams[0].to_list()
    return [(words[i],counts[i]) for i in range(len(words))]

# print(ngramize('#algorithms', 1, 3))