from brownie import FedChainLocal, accounts
import random
import sys

my_account = accounts.add()

def main():
    rand_num = random.randint(1,10)
    rand_num2 = random.randint(1,10)
    contract = FedChainLocal.at("0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87")
    transact = contract.store_param(rand_num,rand_num2,{"from":my_account})
    transact.wait(1)
    print("Data: ", rand_num, " successfully Stored!")
    print("#")