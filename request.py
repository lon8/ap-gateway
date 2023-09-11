import json
import requests


req = requests.get('http://127.0.0.1:8000/')

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(req.text, file, indent=4, ensure_ascii=False)

print(req.text)