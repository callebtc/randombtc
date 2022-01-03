import requests

from .base import HashSource


class MempoolSpace(HashSource):
    source_name: str = "Mempool.space"
    source_entropy: str = ""
    current_block: dict = {}
    current_hash: str

    def __init__(self, source_entropy="blockhash"):
        self.source_entropy = source_entropy
        super().__init__(self.source_name)

    def get_last_block(self):
        resp = requests.get("https://mempool.space/api/blocks")
        if resp.status_code != 200:
            raise Exception("Error: {}".format(resp.status_code))
        json_data = resp.json()
        self.current_block = json_data[0]

    def get_timestamp(self):
        self.get_last_block()
        return self.current_block["timestamp"]

    def get_blockhash(self):
        self.get_last_block()
        self.current_hash = self.current_block["id"]
        return self.current_hash

    def get_merkle_root(self):
        self.get_last_block()
        self.current_hash = self.current_block["merkle_root"]
        return self.current_hash

    def entropy(self) -> str:
        if self.source_entropy == "blockhash":
            return self.get_blockhash()
        elif self.source_entropy == "merkle_root":
            return self.get_merkle_root()
        else:
            raise Exception(
                "Invalid source_entropy: {}".format(self.source_entropy))
