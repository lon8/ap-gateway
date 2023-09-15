from fastapi import APIRouter, HTTPException
import requests
from src.tasks import process_request

router = APIRouter()


@router.get("/vk")
def vk():
    response = requests.get('http://127.0.0.1:8000')
    response.raise_for_status()
    return response.json()

@router.get("/instagram")
def instagram():
    response = requests.get('http://127.0.0.1:8080')
    response.raise_for_status()
    return response.json()

@router.post('/api/get_data')
async def process_request_view(payload : dict):
    result = process_request.delay(payload)
    return {"task_id": result.id, 'result': result.result}