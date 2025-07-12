from pydantic import BaseModel
from enum import Enum
from typing import List, Dict

class Network(str, Enum):
    BITCOIN= "bitcoin"
    ETHEREUM= "ethereum"
    POLYGON= "polygon"
    ARBITRUM= "arbitrum"

class UpgradeType(str, Enum):
    GOVERNANCE= "governance"
    IMPLEMENTATION= "implementation"
    PARAMETER= "parameter"



class InputParams(BaseModel):
    network: Network
    protocol_addresses: List[str]
    upgrade_types: List[UpgradeType]
    risks_thresholds: Dict[str, float]
    time_horizon: str
    asset_pairs: List[Dict[str, str]]
