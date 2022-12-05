import json

json_file_path = r'mu_responses_json.json'
with open(json_file_path) as f:
    invalid_json = f.read()
valid_json = invalid_json.replace("'", '"')
json.loads(valid_json)
