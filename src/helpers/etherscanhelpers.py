from typing import Optional
from eth_utils import to_checksum_address
import requests
from web3 import Web3
from config.apiConfig import settings

api_key = settings.ETHERSCAN_API_KEY
BASE_URL = "https://api.etherscan.io/api"

def get_storage_at(proxy_address: str, position: str):
    try:
        params = {
            "module": "proxy",
            "action": "eth_getStorageAt",
            "address": proxy_address,
            "position": position,
            "tag": "latest",
            "apikey": api_key
        }

        print(f"[DEBUG] Fetching storage at slot {position} for {proxy_address}")
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        print(f"[DEBUG] eth_getStorageAt response: {data}")

        if "result" in data and data["result"]:
            return data["result"]
        else:
            print(f"[ERROR] Invalid storage response: {data}")
            return None
    except Exception as e:
        print(f"[ERROR] Exception in get_storage_at(): {e}")
        return None

def get_implementation_address(proxy_address: str) -> Optional[str]:
    try:
        slot = "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc"
        result = get_storage_at(proxy_address, slot)

        if result and len(result) == 66:
            impl = "0x" + result[-40:]
            checksum = Web3.to_checksum_address(impl)
            print(f"[INFO] Proxy implementation address: {checksum}")
            return checksum

        print(f"[INFO] No proxy implementation found for {proxy_address}")
        return None

    except Exception as e:
        print(f"[ERROR] Exception in get_implementation_address(): {e}")
        return None
