from brownie import FedChainLocal, accounts

account = accounts[0]

def main():
    print("Deploying Contract")
    fedChainLocal = FedChainLocal.deploy({"from": account})
    print("Contract Deployed")
    print("----")
    print(fedChainLocal)
    print("----")
    for i in range(100):
        accounts.add()
        print('Created Account ', i)
    print("Process Done")