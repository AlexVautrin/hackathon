from fastapi import APIRouter, HTTPException
from app.utils.data_loader import load_yaml
import random

router = APIRouter()

@router.get("/recommandation", tags=['Dijon'])
async def recommandation():
    recommendations = load_yaml('recommandations.yaml').get("recommandations", [])
    if not recommendations:
        raise HTTPException(status_code=404, detail="Aucune recommandation disponible")
    return {"recommandation": random.choice(recommendations)}
