from config.apiConfig import settings
from fastapi import FastAPI

from controller import monitor_controller

app = FastAPI()
app.include_router(monitor_controller.router, prefix="/monitor")

@app.get("/")
def root():
    return {"message" : "Protocol upgrade monitor is running"}

print(settings.ETHERSCAN_API_KEY)
print(settings.COINGECKO_API_KEY)
print(settings.TALLY_API_KEY)


# def create_app():
#     app = FastAPI(title="Protocol Upgrade Monitor")
#     blockchain_gateway = EtherscanGateway()
#     blockchain_service = BlockchainService(blockchain_gateway)
#     blockchain_router = get_blockchain_router(blockchain_service)

#     blockchain_router = get_blockchain_router(blockchain_service)
#     app.include_router(blockchain_router)
#     return app

# app = create_app()

# @app.on_event("startup")
# async def startup_event():
#     print("Application started")
