import requests

def get_request(url_api):
    request = requests.get(url_api)
    return request.json()
