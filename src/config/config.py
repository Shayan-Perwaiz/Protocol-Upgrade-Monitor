import os 
from dotenv import load_dotenv
from typing import TypedDict

class ConfigAPI(TypedDict):
    ETHERSCAN_API_KEY: str
    COINGECKO_API_KEY: str


load_dotenv()

API_KEYS: ConfigAPI = {"ETHERSCAN_API_KEY" : os.getenv("ETHERSCAN_API_KEY"),
                        "COINGECKO_API_KEY" : os.getenv("COINGECKO_API_KEY")}

# ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
# COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")