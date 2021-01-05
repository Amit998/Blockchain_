import hashlib

class Block:
    def __init__(self,prev_hash,transaction):
        self.transactions=transaction
        self.prev_hash=prev_hash
        string_to_hash="".join(transaction) + prev_hash
        self.block_hash=hashlib.sha256(string_to_hash.encode()).hexdigest()
