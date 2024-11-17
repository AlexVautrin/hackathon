from fastapi import APIRouter
from app.utils.api_requests import get_request
from app.utils.helpers import isResponseEmpty, create_dict_gravite
import os
from dotenv import load_dotenv

router = APIRouter()

load_dotenv()

requete_gravite = os.getenv('URL_API_GRAVITE')

@router.get("/niveau_alerte", tags=['Dijon'])
async def niveau_alerte():
    response = get_request(requete_gravite)
    gravite = "ras" if isResponseEmpty(response) else response["niveauGravite"]
    date_debut = None if isResponseEmpty(response) else response["arrete"]["dateDebutValidite"]
    date_fin = None if isResponseEmpty(response) else response["arrete"]["dateFinValidite"]
    return create_dict_gravite(gravite, date_debut, date_fin)
