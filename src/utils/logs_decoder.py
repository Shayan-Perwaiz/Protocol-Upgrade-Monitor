import json
from pathlib import Path
from typing import List, Dict

from web3 import Web3

def load_abi(filename: str) -> List[Dict]:
    abi_path = Path(__file__).resolve().parent.parent / "abis" / filename
    with abi_path.open("r") as f:
        return json.load(f)
    
def decode_logs(raw_logs: List[Dict], abi: List[Dict]) -> List[Dict]:
    web3 = Web3()
    contract = web3.eth.contract(abi=abi)

    decoded= []
    for log in raw_logs:
        try:
            event = contract.events._find_matching_event_abi(log["topics"][0])
            decoded_logs = contract.events[event["name"]]().processLog(log)
            decoded.append(dict(decoded_logs))
        except Exception as e:
            decoded.append({"error" : str(e), "raw_log" : log})   
    return decoded         
        