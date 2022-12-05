from sense2vec import Sense2Vec

# Stuck on this right now, getting output errors.
#import spacy

# nlp = spacy.load("en_core_web_sm")
# s2v = nlp.add_pipe("sense2vec")
# s2v.from_disk("/path/to/s2v_reddit_2015_md")

s2v = Sense2Vec().from_disk("mu_responses_json.json")
most_similar = s2v.most_similar("artist|NOUN", n=10)

#Sense2Vec.from_disk("")