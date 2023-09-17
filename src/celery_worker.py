import json
from celery import Celery
import requests

celery = Celery(
    'myapp',
    broker='redis://localhost:6379/0',  # URL Redis сервера для Celery
    backend='redis://localhost:6379/0'  # URL Redis сервера для результатов выполнения задач
)

json_data = {
    'search_query': 'some_search_query',
}

def valid_token(token : str, uid : int):
    return # Здесь будет функция для проверки валидности токена

@celery.task()
def process_task(payload : dict):
    if payload['social'] == 1:
        response = requests.post('http://127.0.0.1:4000/', json=payload)
        
        return response.json()
    elif payload['social'] == 2:
        response = requests.post('http://127.0.0.1:5000/', json=payload)
        
        return response.json()
    else:
        error = {
            'status_code': 404,
            'msg': 'NotFound'
        }
        return error
    
if __name__ == '__main__':
    celery.start()
