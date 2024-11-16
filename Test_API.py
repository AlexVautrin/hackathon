import os
import requests
from dotenv import load_dotenv

#TODO: recuperer recommandations en cas de sécheresse 

load_dotenv()

commune = os.getenv('COMMUNE')
latitude = os.getenv('LATITUDE')
longitude = os.getenv('LONGITUDE')

requete_gravite = f'https://api.vigieau.gouv.fr/api/zones?lon={longitude}&lat={latitude}&commune={commune}'
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


print(get_nappes())
print(get_riviere())
print(create_dict_gravite(get_gravite(), get_date_debut(), get_date_fin()))