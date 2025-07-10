from config import config
from fastapi import FastAPI

print(config.API_KEYS['COINGECKO_API_KEY'])
print(config.API_KEYS['ETHERSCAN_API_KEY'])

app = FastAPI(title = "Protocol Upgrade Monitor")