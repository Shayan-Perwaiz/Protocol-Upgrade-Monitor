# src/service/risk_analysis/risk_scoring_service.py

from repository.marketData.coinGecko_repo import get_token_market_data
from service.market_analysis.volatility_service import calculate_volatility
from repository.GovernanceProposal.governanceProposal_repo import get_recent_proposals

def calculate_risk_score(token_id: str, protocol_id: str) -> dict:
    proposals = get_recent_proposals(protocol_id)
    governance_risk = "Active proposal in progress" if proposals else "No active proposals"
    governance_score = 20 if proposals else 0

    volatility = calculate_volatility(token_id)
    if volatility > 10:
        price_risk = f"Very high volatility ({volatility}%)"
        price_score = 40
    elif volatility > 5:
        price_risk = f"High volatility ({volatility}%)"
        price_score = 25
    else:
        price_risk = f"Low volatility ({volatility}%)"
        price_score = 10

    market_data = get_token_market_data(token_id)
    try:
        market_cap = market_data["market_data"]["market_cap"]["usd"]
        if market_cap < 1e7:
            liquidity_risk = f"Low market cap (${market_cap:,})"
            liquidity_score = 30
        elif market_cap < 1e9:
            liquidity_risk = f"Moderate market cap (${market_cap:,})"
            liquidity_score = 15
        else:
            liquidity_risk = f"High market cap (${market_cap:,})"
            liquidity_score = 5
    except Exception:
        liquidity_risk = "No market cap info"
        liquidity_score = 20

    total_score = governance_score + price_score + liquidity_score

    return {
        "risk_score": total_score,
        "details": {
            "governance_risk": governance_risk,
            "price_risk": price_risk,
            "liquidity_risk": liquidity_risk,
        },
    }
