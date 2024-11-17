from fastapi import APIRouter
from app.utils.api_requests import get_request
import os
from dotenv import load_dotenv

router = APIRouter()

load_dotenv()

requete_meteo = os.getenv('URL_API_METEO')

@router.get("/meteo", tags=['Dijon'])
async def meteo():
    response = get_request(requete_meteo)
    if "hourly" not in response:
        return response

    hourly_data = response["hourly"]
    grouped_data = [
        {
            "time": hourly_data["time"][i],
            "temperature": hourly_data["temperature_2m"][i],
            "humidity": hourly_data["relative_humidity_2m"][i],
            "precipitation": hourly_data["precipitation"][i],
        }
        for i in range(len(hourly_data["time"]))
    ]
    return grouped_data
