from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()


@router.get("/vk")
def vk():
    response = requests.get('http://vk-service:3000')
    response.raise_for_status()
    return response.json()

@router.get("/instagram")
def instagram():
    response = requests.get('http://instagram-service:4000')
    response.raise_for_status()
    return response.json()