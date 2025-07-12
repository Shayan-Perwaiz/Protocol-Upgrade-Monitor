from fastapi import APIRouter, Query
from service.monitor_service import EtherscanMonitorService



router = APIRouter()    

monitor_service = EtherscanMonitorService()

@router.get("/logs")
def get_logs(address : str = Query(..., description="Contract address to monitor"),
             topic0 : str = Query(None, description="Event Signature Topic (optional)")):
    return monitor_service.fetchUpgateEvents(address=address, topic0=topic0)



