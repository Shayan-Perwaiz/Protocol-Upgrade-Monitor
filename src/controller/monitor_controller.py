from fastapi import APIRouter, Query
from service.etherscan_service.monitor_service import fetchUpgateEvents


router = APIRouter()    

@router.get("/decode-logs")
def decode_logs(address : str = Query(..., description="Contract address to monitor"),
             topic0 : str = Query(None, description="Event Signature Topic (optional)")):
    return fetchUpgateEvents(address=address, topic0=topic0)



