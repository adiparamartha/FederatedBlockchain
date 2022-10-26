from brownie import FedChainLocal, accounts

my_account = accounts[1]

def main():
    contract = FedChainLocal.at("0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87")
    val = contract.aggregate_param({"from":my_account})
    clientID = val[0]
    param = val[1]
    sumParam = 0
    totParam = len(param)

    for i in param:
        sumParam = sumParam + int(i)
    avgParam = sumParam / totParam

    print("Overall: ", val)
    print("Param (n): ", totParam)
    print("Sum: ", sumParam)
    print("Avg: ", avgParam)
