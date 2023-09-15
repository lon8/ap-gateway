from celery import Celery
import requests

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_request(payload : dict):
    # Ваша логика обработки запроса
    # Здесь вы можете использовать service_name для определения, к какому сервису направить запрос
    # request_data содержит данные запроса

    service = payload['social']
    
    # Пример обработки
    if service == 1:
        # Отправить запрос к сервису vk
        result = requests.post('127.0.0.1:3000', json=payload)
        return result
        pass
    elif service == 2:
        result = requests.post('127.0.0.1:4000', json=payload)
        pass
    else:
        return "Bad request"
        pass

    