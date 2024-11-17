import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from app.utils.data_loader import load_json
from app.utils.api_requests import get_request
from app.utils.helpers import isResponseEmpty

router = APIRouter()

load_dotenv()

# Fonction pour récupérer la gravité (utilisant get_gravite())
def get_gravite():
    response = get_request(os.getenv('URL_API_GRAVITE'))
    gravite = "ras" if isResponseEmpty(response) else response["niveauGravite"]
    return gravite

@router.get("/message", tags=['Dijon'])
async def message():
    messages = load_json('message.json')
    gravite = get_gravite()
    if gravite in messages:
        return {"message": messages[gravite]}
    raise HTTPException(status_code=404, detail="Message non trouvé")
