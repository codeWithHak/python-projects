from random import randint 

# a list that will store all accounts
all_accounts = []   

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
    
    all_accounts.append(account)
    print(f"Congrats {acc_title} your account has been opened successfully!")
    print(all_accounts)
open_account()