import os 
from dotenv import load_dotenv


load_dotenv()
class Settings:
    ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
    COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
    TALLY_API_KEY = os.getenv("TALLY_API_KEY")
    

settings = Settings()