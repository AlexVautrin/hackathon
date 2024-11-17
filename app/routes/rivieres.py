from fastapi import APIRouter
from app.utils.api_requests import get_request
import os
from dotenv import load_dotenv

router = APIRouter()

load_dotenv()

requete_riviere = os.getenv('URL_API_RIVIERES')

@router.get("/rivieres", tags=['Dijon'])
async def niveau_riviere():
    return get_request(requete_riviere)["data"]
