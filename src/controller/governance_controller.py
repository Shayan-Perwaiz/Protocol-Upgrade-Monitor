from service.GovernanceService.governance_service import analyze_governance_risk
from fastapi import APIRouter, Query

router = APIRouter(prefix="/governance", tags=["Governance"])

@router.get("/risk")
def get_governance_risk(governor_id: str = Query(..., description="Tally Governor ID")):
    result = analyze_governance_risk(governor_id)
    return result
