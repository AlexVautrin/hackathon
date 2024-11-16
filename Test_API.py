import os
import json
import requests
from dotenv import load_dotenv

#TODO: recuperer recommandations en cas de sécheresse 

load_dotenv()

requete_gravite = os.getenv('URL_API_GRAVITE')
requete_nappes = os.getenv('URL_API_NAPPES')
requete_riviere = os.getenv('URL_API_RIVIERES')
requete_meteo = os.getenv('URL_API_METEO')


def get_request(url_api) :
    request = requests.get(url_api)
    result = request.json()
    return result

def isResponseEmpty(response):
    if (response == []):
        return True
    else :
        return False

def get_gravite():
    response = get_request(requete_gravite)
    if (isResponseEmpty(response) is True) :
        gravite = "RAS"
    else :
        gravite =  response["niveauGravite"]
    return gravite

def get_date_debut():
    response = get_request(requete_gravite)
    if (isResponseEmpty(response) is True):
        date_debut = None
    else :
        date_debut =  get_request(requete_gravite)["arrete"]["dateDebutValidite"]
    return date_debut

def get_date_fin():
    response = get_request(requete_gravite)
    if (isResponseEmpty(response) is True):
        date_fin = None
    else :
        date_fin = get_request(requete_gravite)["arrete"]["dateFinValidite"]
    return date_fin

def create_dict_gravite(gravite, date_debut, date_fin):
    dict_gravite = {
        "gravite": gravite,
        "date_debut": date_debut,
        "date_fin": date_fin
    }

    return dict_gravite

def get_nappes():
    return get_request(requete_nappes)

def get_riviere():
    return get_request(requete_riviere)

def get_meteo():
    response = get_request(requete_meteo)
    if "hourly" not in response:
        return response

    hourly_data = response["hourly"]
    times = hourly_data.get("time", [])
    temperatures = hourly_data.get("temperature_2m", [])
    humidities = hourly_data.get("relative_humidity_2m", [])
    precipitations = hourly_data.get("precipitation", [])

    grouped_data = []
    for i in range(len(times)):
        temperature = temperatures[i] if i < len(temperatures) else None
        humidity = humidities[i] if i < len(humidities) else None
        precipitation = precipitations[i] if i < len(precipitations) else None

        if temperature is not None or humidity is not None or precipitation is not None:
            grouped_data.append({
                "time": times[i],
                "temperature": temperature,
                "humidity": humidity,
                "precipitation": precipitation
            })

    response["hourly"] = grouped_data
    return response




print(get_nappes())
print(get_riviere())
print(create_dict_gravite(get_gravite(), get_date_debut(), get_date_fin()))
print(json.dumps(get_meteo(), indent=2))