from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint
from Blockchain import BlockChain



if __name__ == '__main__':
    sender='sender'
    receiver='recevier'
    amount=100
    type="Transfer"

    wallet=Wallet()
    fraudWallet=Wallet()

    transaction=wallet.createTransaction(receiver,amount,type)

    pool=TransactionPool()

    if pool.transactionExists(transaction)==False:
        pool.addTransaction(transaction)
    
    blockchain=BlockChain()

    lastHash=BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()

    blockCount=blockchain.blocks[-1].blockCount+1
    
    block=wallet.createBlock(pool.transactions,lastHash,blockCount)
    
    

    if not blockchain.lastBlockHashValid(block):
        print("last Block is not valid")
    if not blockchain.blockCountValid(block):
        print("Block Count is not valid")
    
    if blockchain.blockCountValid(block) and blockchain.lastBlockHashValid(block):
        pprint.pprint(blockchain.toJson())


    # signatureValid=wallet.signatureValid(block.payload(),block.signature,wallet.publicKeyString())

    # print(signatureValid)
    # pprint.pprint(block.toJson())


    
    # print(block.toJson())

    # block=Block(pool.transactions,'lastHash','forger',1)


    # print(block.toJson())

    
    # print(pool.transaction)

    # signatureValid=wallet.signatureValid(transaction.payload(),transaction.signature,wallet.publicKeyString())

    # print(signatureValid)
    # print(transaction.payload())
    # transaction = Transaction(sender,receiver,amount,type)

    # print(transaction.toJson())

    # wallet=Wallet()
    # signature=wallet.sign(transaction.toJson())
    # # print(signature)


    # transaction.sign(signature)

    # # print(transaction.toJson())

    # signatureValid=wallet.signatureValid(transaction.payload(),signature,wallet.publicKeyString())

    # print(signatureValid)

