import numpy as np
from repository.marketData.coinGecko_repo import get_price_history

def calculate_volatility(token_id: str, days: int = 7) -> float:
    data = get_price_history(token_id, days)
    prices = [p[1] for p in data.get("prices", [])]

    if len(prices) < 2:
        return 0.0

    log_returns = np.diff(np.log(prices))
    volatility = np.std(log_returns) * 100
    return round(volatility, 2)