from hashlib import sha256
# from typing import Text
import time

# print(sha256('AMIT'.encode("ascii")).hexdigest())

MAX_NONCE=100000000

def SHA256(text):
  return sha256('AMIT'.encode("ascii")).hexdigest()

# print(SHA256("AMIT"))

def mine(block_number,transcation,previous_hash,prefix_zeros):
    # nonce=1
    prefix_str='0'*prefix_zeros

    for nonce in range(MAX_NONCE):
        Text=str(block_number) + transcation + previous_hash + str(nonce)
        new_hash=SHA256(Text)
        if(new_hash.startswith(prefix_str)):
            return new_hash

if __name__ == "__main__":
    transaction='''
    AMIT->Kuntal->20,
    KUntal->Dip->200
    '''
    difficulty=4
    start=time.time()
    print("start mining")
    

    new_hash=mine(5,transaction,'7f40340b07aa241d6db11bb16662cfe9410af8c97d49be3050391e84a3943fec',difficulty)
    total_time=str(time.time()-start)
    print(new_hash,start)