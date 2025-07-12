from fastapi import APIRouter, Query
from service.risk_analysis.risk_scoring_service import calculate_risk_score

router = APIRouter()

@router.get("/risk-score")
def get_risk_score(
    token_id: str = Query(..., description="CoinGecko token ID"),
    protocol_id: str = Query(..., description="Tally governance protocol ID")
):
    result = calculate_risk_score(token_id, protocol_id)
    return result