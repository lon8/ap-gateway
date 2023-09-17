import json
import requests

json_data = {
    'search_query': 'votanak',
    'social': 1,
    'user_id': 52
}

req = requests.post('127.0.0.1:8000/', json=json_data)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(req.json(), file, indent=4, ensure_ascii=False)
