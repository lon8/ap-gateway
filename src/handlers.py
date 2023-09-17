import asyncio
from fastapi import APIRouter, HTTPException
import requests

from src.celery_worker import process_task

router = APIRouter()

@router.post('/vk_analytics')
async def parse_kernel(payload: dict):
    payload['social'] = 1
    result = process_task.delay(payload)
    task_result = await get_result(result)  # Ждем завершения задачи
    return task_result
    
@router.post('/instagram_analytics')
async def parse_kernel(payload: dict):
    payload['social'] = 2
    result = process_task.delay(payload)
    task_result = await get_result(result)  # Ждем завершения задачи
    return task_result

async def get_result(result):
    while not result.ready():
        await asyncio.sleep(1)  # Ждем, пока задача не будет завершена
    return result.result
