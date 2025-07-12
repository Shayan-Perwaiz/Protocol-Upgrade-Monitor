import requests
from config.apiConfig import settings

TALLY_API_KEY = settings.TALLY_API_KEY
TALLY_BASE_URL = "https://api.tally.xyz/query"

headers = {
    "Content-Type": "application/json",
    "Api-Key": TALLY_API_KEY
}

def get_recent_proposals(governor_id: str, limit: int = 20) -> list:
    query = {
        "query": """
        query GovernanceProposals($governorId: String!, $limit: Int!) {
          proposals(input: {governorId: $governorId, pagination: {limit: $limit}}) {
            nodes {
              proposalId
              title
              state
              createdAt
              eta
              votes {
                against
                for
              }
            }
          }
        }
        """,
        "variables": {
            "governorId": governor_id,
            "limit": limit
        }
    }
