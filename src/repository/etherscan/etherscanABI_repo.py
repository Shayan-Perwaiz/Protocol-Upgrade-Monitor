import os 
import requests
from config.apiConfig import settings
from helpers.etherscanhelpers import get_implementation_address


BASE_URL = "https://api.etherscan.io/api"
api_key = settings.ETHERSCAN_API_KEY

def getABI(address : str) -> dict:
    impl_address = get_implementation_address(address)
    actual_address = impl_address if impl_address and impl_address != "0x0000000000000000000000000000000000000000" else address
    print(f"[INFO] Using address for ABI fetch: {actual_address}")

    params = {
        "module" : "contract",
        "action" : "getabi",
        "address" : actual_address,
        "apikey" : api_key
        }
    response = requests.get(BASE_URL, params=params)
    data = response.json()  
    print(f"[DEBUG] ABI fetch response: {data}")  

    if data["status"] != "1":
        raise Exception(f"Failed to fetch ABI for {address}: {data['message']}")
        
    return data["result"]