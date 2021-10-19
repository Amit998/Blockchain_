from TransactionPool import TransactionPool
from Blockchain import BlockChain
from Wallet import Wallet

class Node():

    def __init__(self):
        self.transitionPool=TransactionPool()
        self.wallet=Wallet()
        self.blockChain=BlockChain()