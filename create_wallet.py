import os
from neo3.wallet.wallet import DiskWallet

def main():
    if os.path.exists("wallet.json"):
        print("wallet.json already exists.")
        return

    w = DiskWallet.default(path="wallet.json", name="test_wallet")
    account = w.account_new(label="default", is_default=True)
    w.save("password123")
    
    print("Created wallet.json. Password: 'password123'")
    print(f"Address: {account.address}")
    
if __name__ == "__main__":
    main()
