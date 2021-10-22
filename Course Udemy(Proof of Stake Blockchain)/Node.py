from TransactionPool import TransactionPool
from Blockchain import BlockChain
from Wallet import Wallet
from SocketCommunication import SocketCommunication
class Node():

    def __init__(self,ip,port):
        self.p2p=None
        self.ip=ip
        self.port=port

        self.transitionPool=TransactionPool()
        self.wallet=Wallet()
        self.blockChain=BlockChain()
    
    def startP2P(self):
        self.p2p=SocketCommunication(self.ip,self.port)
        self.p2p.startSocketCommunication()
        