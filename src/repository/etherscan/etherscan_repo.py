import requests
from config.apiConfig import settings
from typing import Optional

BASE_URL = "https://api.etherscan.io/api"
api_key = settings.ETHERSCAN_API_KEY

def getLogs(address : str, from_block : str =  "latest", to_block : str = "latest", topic0 : Optional[str] = None):
    params = {
        "module" : "logs",
        "action" : "getLogs",
        "address" : address,
        "from_block" : from_block,
        "to_block" : to_block,
        "apikey" : api_key
        }    

    if topic0:
        params["topic0"] = topic0

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    return data    