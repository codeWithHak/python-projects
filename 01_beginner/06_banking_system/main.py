from bank import open_account, deposit_amount

print(f"\n{'-'*20} Welcome to Saylani Islamic Bank {'-'*20}\n")

while True:
    
    try:
        print("1) Open new account")
        print("2) Deposit Money in your account")
        user_input = int(input(("Select any option from above: ")))
        
        if user_input == 1:
            open_account()
            break
            
        elif user_input == 2:
            deposit_amount()
            break
        
    except ValueError:
        print(f" !!! Invalid Value !!! ")
        
    