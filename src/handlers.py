from fastapi import APIRouter, HTTPException
import requests

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