from repository.etherscan_repo import EtherscanRepo

class EtherscanMonitorService:

    def __init__(self):
        self.etherscanRepo = EtherscanRepo()

    def fetchUpgateEvents(self, address : str, topic0 : str = None):
        logs = self.etherscanRepo.getLogs(address=address, topic0=topic0)
        return logs    
