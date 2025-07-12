from service.market_analysis.volatility_service import calculate_volatility
from fastapi import APIRouter, FastAPI, Query

router = APIRouter()

@router.get("/volatility")
def get_volatility(token_id: str = Query(..., description="CoinGecko token ID (e.g., uniswap)")):
    volatility = calculate_volatility(token_id)
    return {
        "token_id": token_id,
        "volatility_score": volatility
    }