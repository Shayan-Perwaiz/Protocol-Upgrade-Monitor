from pydantic import BaseModel
from typing import List, Dict

class OutputParams(BaseModel):
    upgrade_risk_score : float
    expected_volatility_impact : Dict
    liquidity_shift_prediction : Dict
    execution_timing : Dict
    portfolio_rebalancing : List[Dict]
    risk_mitigation : List[str]