import hashlib
import json
from time import time
from hashlib import sha256

x = 5
y = 0  # We don't know what y should be yet...
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1
print(f'The solution is y = {y}')
print(hash(5 * 21))



Class Blockchain(object):
    def __init__(self):
        self.chain[]
        self.current_transactions = []

    def new_block(self, proof, previous_hash=None):
        block ={
                "index":len(self.chain) + 1, 
                "timestamp" : time(),
                "transactions" : self.current_transactions,
                "proof": proof,
                "previous_hash": previous_hash or self.hash(self.chain[-1]), 
                
            }
        self.current_transactions = []

        self.chain.append(block)
        return block
        

    def new_transaction(self,sender, recipient, amount):

        self.current_transactions.append( {"sender":sender, "recipient":recipient,"amount":amount,})

         return self.last_block['index'] + 1

        
    def last_block(self):

        return self.chain[-1]

    def hash(block):

        pass


        
