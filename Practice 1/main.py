import hashlib
from block import Block

blockchain=[]

# hash = hashlib.sha256("secret Message ".encode()).hexdigest()
# print(hash)

genesis_block=Block("Canceller on th brink...",["stoshi sent 1 BTC ","Maria sent 5 BTC to jenny","Satoshi send 5 BTC to Hal inney"])

second_block=Block(genesis_block.block_hash,["Amit Sent 5 BTC to Bratati","Jhon cena Sent 2BTC to Akbar"])


third_block=Block(second_block.block_hash,["Virat Sent 5 BTC to Anushka","sunil chettri Sent 2BTC to sandesh"])


print("Block hash Genesis Block")
print(genesis_block.block_hash)

print("Block hash Second Block")
print(second_block.block_hash)


print("Block hash third Block")
print(third_block.block_hash)