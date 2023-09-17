import asyncio
from fastapi import APIRouter, HTTPException
import requests

from src.celery_worker import process_task

router = APIRouter()

@router.post('/')
async def parse_kernel(payload: dict):
    result = process_task.delay(payload)
    task_result = await get_result(result)  # Ждем завершения задачи
    return {"task_id": result.id, "task_result": task_result}
    
    # Debug
    
    #if payload['social'] == 1:
    #    response = requests.post('http://127.0.0.1:4000/', json=payload)
    #    
    #    return response.json()
    #elif payload['social'] == 2:
    #    response = requests.post('http://127.0.0.1:5000/', json=payload)
    #    
    #    return response.json()
    #else:
    #    error = {
    #        'search_query': payload['search_query'],
    #        'keyError': 'Key "social" is false'
    #    }
    #    return error


async def get_result(result):
    while not result.ready():
        await asyncio.sleep(1)  # Ждем, пока задача не будет завершена
    return result.result
