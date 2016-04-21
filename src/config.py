import json

config = {}

with open('../config.json') as f:
    config = json.load(f)