from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action='ignore')

import gensim
from gensim.models import Word2Vec

sample = open("mu_responses_txt.txt", encoding="utf8")
s = sample.read()
f = s.replace("\n", " ")
data = []
for i in sent_tokenize(f):
    temp = []

    # tokenize the sentence into words
    for j in word_tokenize(i):
        temp.append(j.lower())

    data.append(temp)

# Create CBOW model
model1 = gensim.models.Word2Vec(data, min_count=1,
                                vector_size=100, window=5)
print("Cosine similarity between 'alice' " +
               "and 'wonderland' - CBOW : ",
    model1.wv.similarity('alice', 'wonderland'))

print("Cosine similarity between 'alice' " +
      "and 'machines' - CBOW : ",
      model1.wv.similarity('alice', 'machines'))

# Create Skip Gram model
model2 = gensim.models.Word2Vec(data, min_count=1, vector_size=100,
                                window=5, sg=1)

# Print results
print("Cosine similarity between 'network' " +
      "and 'node' - Skip Gram : ",
      model2.wv.similarity('network', 'node'))

print("Cosine similarity between 'network' " +
      "and 'system' - Skip Gram : ",
      model2.wv.similarity('network', 'system'))
