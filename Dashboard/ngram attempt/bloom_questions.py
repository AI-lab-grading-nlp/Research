from huggingface_hub import InferenceApi

inference = InferenceApi("bigscience/bloom",token='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')

import time
import random

def infer(prompt,
          max_length = 250,
          top_k = 50,
          num_beams = 0,
          no_repeat_ngram_size = 0,
          top_p = 0.7,
          seed= random.randint(0,1000000),
          temperature=0.2,
          greedy_decoding = False,
          return_full_text = False):
    

    top_k = None if top_k == 0 else top_k
    do_sample = False if num_beams > 0 else not greedy_decoding
    num_beams = None if (greedy_decoding or num_beams == 0) else num_beams
    no_repeat_ngram_size = None if num_beams is None else no_repeat_ngram_size
    top_p = None if num_beams else top_p
    early_stopping = None if num_beams is None else num_beams > 0

    params = {
        "max_new_tokens": max_length,
        "top_k": top_k,
        "top_p": top_p,
        "temperature": temperature,
        "do_sample": do_sample,
        "seed": seed,
        "early_stopping":early_stopping,
        "no_repeat_ngram_size":no_repeat_ngram_size,
        "num_beams":num_beams,
        "return_full_text":return_full_text,
        "n_gram_size": 1
    }
    
    s = time.time()
    response = inference(prompt, params=params)
    #print(response)
    proc_time = time.time()-s
    #print(f"Processing time was {proc_time} seconds")
    return response


def create_prompt(answers):

    prompt = ''''''
    answers = answers.split('\n')
    for i, answer in enumerate(answers):
        prompt += f'''Prompt {i+1}: {answer}\n'''
    fin = '''Question: What questions are the above prompts answering? \n Answer: '''
    
    prompt += fin
    
    print(prompt)
    return prompt