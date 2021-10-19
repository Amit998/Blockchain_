from Block import Block
from BlockchainUtils import BlockchainUtils

class BlockChain():


    def __init__(self):
        self.blocks=[Block.genesis()]

    
    def addBlock(self,block):
        self.blocks.append(block)
    

    def toJson(self):
        data={}
   
        jsonBlocks=[]
        for transaction in self.blocks:
            jsonBlocks.append(transaction.toJson())
        data['blocks']=jsonBlocks

        return data
    def blockCountValid(self,block):
        if self.blocks[-1].blockCount==block.blockCount-1:
            return True
        else:
            return False
    def lastBlockHashValid(self,block):
        latestBlockChainBlockHash=BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        if latestBlockChainBlockHash==block.lastHash:
            return True
        else:
            return False