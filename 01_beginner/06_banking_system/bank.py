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
    
    print("\n-- Provide Credentials Of Your Account --\n")
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
            
    
def withdraw_amount():
    print("\n-- Provide Credentials Of Your Account --\n")
    acc_title = input("Account title: ")
    acc_pin = int(input("Account pin: "))

    for acc in all_accounts:
        if acc_title == acc["acc_title"]:
            
            if acc["acc_pin"] == acc_pin:
                withdraw = int(input("Amount you want to deposit: "))
                if acc["acc_balance"] > withdraw:
                    acc['acc_balance'] -= withdraw
                    print(f"{withdraw} withrawn from {acc_title}")


                    with open(accounts_file, "w") as f:
                        json.dump(all_accounts, f, indent=4)
                        return
                else:
                    print(f"Your current blance is below {withdraw}!")
                    print("Can't withdarw!")
                    return
              
            else:
                print(f"Wrong pin you only have 2 more tries!")
                return
        
    print(f"Account with title {acc_title} dosen't exist!")


def check_balance():
    print("\n-- Provide Credentials Of Your Account --\n")
    acc_title = input("Account title: ")
    acc_pin = int(input("Account pin: "))

    for acc in all_accounts:
        if acc_title == acc["acc_title"]:
            
            if acc["acc_pin"] == acc_pin:
                print(f"Your current balance is {acc["acc_balance"]}")
                return
              
            else:
                print(f"Wrong pin you only have 2 more tries!")
                return
        
    print(f"Account with title {acc_title} dosen't exist!")


def close_account():
    print("\n-- Provide Credentials Of Account You Want To Close --\n")
    acc_title = input("Account title: ")
    acc_pin = int(input("Account pin: "))

    for acc in all_accounts:
        if acc_title == acc["acc_title"]:
            
            if acc["acc_pin"] == acc_pin:
                if acc["acc_balance"] > 0:
                    print(f"Here's your balance {acc["acc_balance"]}")
                    print(f"Bye, Thanks for being a part of Saylani Islamic Bank!")
                    print(f"-- Account Closed --")
                    all_accounts.remove(acc)
                    
                    with open(accounts_file, "w") as f:
                        json.dump(all_accounts, f, indent=4)
                    return
              
            else:
                print(f"Wrong pin you only have 2 more tries!")
                return
        
    print(f"Account with title {acc_title} dosen't exist!")


close_account()