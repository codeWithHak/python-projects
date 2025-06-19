from random import randint 
import os
import json
# a list that will store all accounts



accounts_file = "accounts.json"

def _read_accounts():
    if os.path.exists(accounts_file):
        with open(accounts_file, "r") as f:
            return json.load(f)
    else:
        return []

def _write_accounts(accounts):
    with open(accounts_file, "w") as f:
        json.dump(accounts, f, indent=4)
    
all_accounts = _read_accounts()
            
            
            
# function for openieng user account
def open_account():    
     
    # taking inputs from user
    acc_title = input("Set your account title: ")
    acc_pin = int(input("Set your account pin: "))
    monthly_income = int(input("What's your monthly income: "))
    acc_balance = int(input("What will be your current balance: "))
    acc_id = randint(1000,9999)
    
    account = {
        "acc_title":acc_title,
        "acc_pin":acc_pin,
        "monthly_income":monthly_income,
        "acc_balance":acc_balance,
        "acc_id":acc_id
    }
    
    for acc in all_accounts:
        if acc['acc_title'].strip().lower() == account['acc_title'].strip().lower():
            print(f"Account with title {acc_title} already exists")
            break
        
    else:
        all_accounts.append(account)
        _write_accounts(all_accounts)
        print(f"Congrats {acc_title} your account has been opened successfully!")
        print(all_accounts)
    
# open_account()

def deposit_amount():
    
    print("\n--Provide Credentials Of Your Account--\n")
    acc_title = input("Account title: ")
    acc_pin = int(input("Account pin: "))

    for acc in all_accounts:
        if acc_title == acc["acc_title"]:
            
            if acc["acc_pin"] == acc_pin:
                deposit = int(input("Amount you want to deposit: "))
                if deposit > 0:
                    acc['acc_balance'] += deposit
                    print(f"{deposit} dopositted to {acc_title}")


                    with open(accounts_file, "w") as f:
                        json.dump(all_accounts, f, indent=4)
                        return
                else:
                    print(f"Invalid amount {deposit}!")
                    return
              
            else:
                print(f"Wrong pin you only have 2 more tries!")
                return
        
    print(f"Account with title {acc_title} dosen't exist!")
            
    

deposit_amount()

