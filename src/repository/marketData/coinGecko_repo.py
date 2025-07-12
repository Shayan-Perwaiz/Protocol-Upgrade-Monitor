import requests
from config.apiConfig import settings

COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"
COINGECKO_API_KEY = settings.COINGECKO_API_KEY

headers = {
    "accept": "application/json",
    "x-cg-pro-api-key": COINGECKO_API_KEY
}

def get_token_market_data(token_id: str):
    url = f"{COINGECKO_BASE_URL}/coins/{token_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_price_history(token_id: str, days: int = 7):
    url = f"{COINGECKO_BASE_URL}/coins/{token_id}/market_chart"
    params = {"vs_currency": "usd", "days": days}
    response = requests.get(url, params=params, headers=headers)
    return response.json()