from fastapi import APIRouter
from app.utils.api_requests import get_request
import os
from dotenv import load_dotenv

router = APIRouter()

load_dotenv()

requete_nappes = os.getenv('URL_API_NAPPES')

@router.get("/nappes", tags=['Dijon'])
async def niveau_nappes():
    return get_request(requete_nappes)["data"]
