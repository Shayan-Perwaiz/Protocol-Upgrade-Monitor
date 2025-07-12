from repository.GovernanceProposal.governanceProposal_repo import get_recent_proposals

def analyze_governance_risk(governor_id: str) -> dict:
    proposals = get_recent_proposals(governor_id)

    if not proposals:
        return {
            "governance_risk": "No recent proposals",
            "proposal_count": 0,
            "active_proposals": []
        }

    high_risk_states = ["ACTIVE", "PENDING", "QUEUED"]
    active = [p for p in proposals if p["state"] in high_risk_states]

    return {
        "governance_risk": "High" if len(active) >= 3 else "Moderate" if active else "Low",
        "proposal_count": len(proposals),
        "active_proposals": active
    }
