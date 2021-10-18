from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':
    sender='sender'
    receiver='recevier'
    amount=1
    type="Transfer"
    transaction = Transaction(sender,receiver,amount,type)

    # print(transaction.toJson())

    wallet=Wallet()
    signature=wallet.sign(transaction.toJson())
    # print(signature)


    transaction.sign(signature)
    print(transaction.toJson())

