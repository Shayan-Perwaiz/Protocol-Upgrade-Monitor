from repository.etherscan.etherscan_repo import getLogs
from repository.etherscan.etherscanABI_repo import getABI
from service.etherscan_service.log_decoder import decode_logs_with_abi

def fetchUpgateEvents(address : str, topic0 : str = None):
    logsResponse = getLogs(address=address, topic0=topic0)

    if logsResponse.get("status") != "1":
        raise Exception(f"Failed to get logs : {logsResponse.get('message')}")

    rawLogs = logsResponse["result"]  
    abiJSON = getABI(address=address)

    return decode_logs_with_abi(rawLogs, abiJSON)
