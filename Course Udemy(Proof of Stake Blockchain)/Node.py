from TransactionPool import TransactionPool
from Blockchain import BlockChain
from Wallet import Wallet
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI
from Message import Message
from BlockchainUtils import BlockchainUtils

class Node():

    def __init__(self,ip,port,key=None):
        self.p2p=None
        self.ip=ip
        self.port=port
        self.transitionPool=TransactionPool()
        self.wallet=Wallet()
        self.blockChain=BlockChain()
        if key is not None:
            self.wallet.formKey(key)
    
    def startP2P(self):
        self.p2p=SocketCommunication(self.ip,self.port)
        self.p2p.startSocketCommunication(self)


    def startAPI(self,apiPort):
        self.api=NodeAPI()
        self.api.injectNode(self)
        self.api.start(apiPort)
    
    def handleTransaction(self,transaction):
        data=transaction.payload()
        signature=transaction.signature
        signerPublicKey=transaction.senderPublicKey
        signatureValid=Wallet.signatureValid(data,signature,signerPublicKey)
        transactionExists=self.transitionPool.transactionExists(transaction)
        transactionInBlockExists=self.blockChain.transactionExists(transaction)
        if not transactionExists and not transactionInBlockExists and signatureValid:
            self.transitionPool.addTransaction(transaction)
            message=Message(self.p2p.socketConnector,'TRANSACTION',transaction)

            encodedMessage=BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)
            forginRequired=self.transitionPool.forgerRequired()
            if forginRequired:
                self.forge()
    def handleBlock(self,block):
        forger=block.forger
        blockHash=block.payload()
        signature=block.signature

        blockCountValid= self.blockChain.blockCountValid(block)
        lastBlockHashValid=self.blockChain.lastBlockHashValid(block)
        



    def forge(self):
        forger=self.blockChain.nextForger()
        print(forger)
        print(self.wallet.publicKeyString())
        if forger == self.wallet.publicKeyString():
            print("i am the next forger")
            block=self.blockChain.createBlock(self.transitionPool.transactions,self.wallet)
            self.transitionPool.removeFromPool(block.transactions)
            message=Message(self.p2p.socketConnector,'BLOCK',block)
            encodedMessage=BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)
        else:
            print("i am not the next forger")
  