import json
# Sample food data
def load_foods():
    with open('monngon_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)