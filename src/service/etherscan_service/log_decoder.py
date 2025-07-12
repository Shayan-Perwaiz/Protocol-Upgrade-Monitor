import json
from web3 import Web3
from eth_utils import event_abi_to_log_topic

w3 = Web3()

def decode_logs_with_abi(rawLogs : list, abiJSON : str) -> list:
    abi = json.loads(abiJSON)
    contract = w3.eth.contract(abi=abi)

    decodedLogs = []
    for log in rawLogs:
        try:
            topic0 = log["topics"][0]
            matchedEvent = None
            for item in abi:
                if item.get("type") == "event":
                    if event_abi_to_log_topic(item).hex().lower() == topic0.lower():
                        matchedEvent = item
                        break

            if not matchedEvent:
                raise ValueError("No matching event ABI found for topic0")

            event_abi = matchedEvent
            decoded = contract.events[event_abi["name"]]().process_log(log)   
            decodedLogs.append(dict(decoded))  

        except Exception as e:
            decodedLogs.append({
                "error": str(e),
                "log": log
            })  

    return decodedLogs             
