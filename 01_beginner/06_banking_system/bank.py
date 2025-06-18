from random import randint 
import os
import json
# a list that will store all accounts
accounts_file = "accounts.json"


# function for openieng user account
def open_account():    
     
    # taking inputs from user
    acc_title = input("Set your account title: ")
    acc_pin = input("Set your account pin: ")
    monthly_income = input("What's your monthly income: ")
    acc_balance = input("What will be your current balance: ")
    acc_id = randint(1000,9999)
    
    account = {
        "acc_title":acc_title,
        "acc_pin":acc_pin,
        "monthly_income":monthly_income,
        "acc_balance":acc_balance,
        "acc_id":acc_id
    }
    
 
    if os.path.exists(accounts_file):
        with open(accounts_file, "r") as f:
            all_accounts = json.load(f)
    else:
        all_accounts = []
        
    all_accounts.append(account)
    
    with open(accounts_file, "w") as f:
        json.dump(all_accounts, f, indent=4)
    
        
    print(f"Congrats {acc_title} your account has been opened successfully!")
    print(all_accounts)
    
open_account()