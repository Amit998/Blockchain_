from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from ProofOfStake import ProofOfStake

class BlockChain():
    def __init__(self):
        self.blocks=[Block.genesis()]
        self.accountModel=AccountModel()
        self.pos=ProofOfStake()

    def addBlock(self,block):
        self.executeTransactions(block.transactions)
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
    
    def getCoveredTransactionSet(self,transactions):
        coveredTransactions=[]
        for transaction in transactions:
            if self.transactionCoverd(transaction):
                coveredTransactions.append(transaction)
            else:
                print("Transaction is not covered by sender")
        return coveredTransactions

    

    def transactionCoverd(self,transaction):

        if transaction.type=="EXCHANGE":
            return True
        
        senderBalance=self.accountModel.getBalance(transaction.senderPublicKey)
        if senderBalance >= transaction.amount:
            return True
        else:
            return False

    def executeTransactions(self,transactions):
        for transaction in transactions:
            self.exchangeTransaction(transaction)


    def exchangeTransaction(self,transaction):
        sender=transaction.senderPublicKey
        if transaction.type == 'STAKE':
            sender=transaction.senderPublicKey
            recevier=transaction.receverPublicKey

            if sender == recevier:
                amount=transaction.amount
                self.pos.update(sender,amount)
                self.accountModel.updateBalance(sender,-amount)
            else:
                recevier=transaction.receverPublicKey
                amount=transaction.amount
                self.accountModel.updateBalance(sender,-amount)
                self.accountModel.updateBalance(recevier,amount)
    def nextForger(self):
        lastBlockHash=BlockchainUtils.hash(
            self.blocks[-1].payload()).hexdigest()
        nextForger=self.pos.forger(lastBlockHash)
        return nextForger
    
    def createBlock(self,transactionFromPool,forgerWallet):
        coveredTransactions=self.getCoveredTransactionSet(
            transactionFromPool
        )
        self.executeTransactions(coveredTransactions)
        newBlock=forgerWallet.createBlock(coveredTransactions,BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest(),len(self.blocks))
        self.blocks.append(newBlock)

        return newBlock
    

    def transactionExists(self,transaction):
        for block in self.blocks:
            for blockTransaction in block.transactions:
                if transaction.equals(blockTransaction):
                    return True
                
        return False
