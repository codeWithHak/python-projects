from bank import open_account, deposit_amount, withdraw_amount, check_balance, transfer_amount, close_account, request_loan, view_all_accounts

print(f"\n{'-'*20} Welcome to Saylani Islamic Bank {'-'*20}\n")

while True:
    
    try:
        print("1) Open new account")
        print("2) Deposit Money in your account")
        print("3) Withdraw Money from your account")
        print("4) Check your current balance")
        print("5) Transfer Money from your account to another account")
        print("6) Close your account")
        print("7) Request Loan")
        print("\n999) View All Accounts (!!! Only For Admins !!!)\n")
        
        user_input = int(input(("Select any option from above: ")))
        
        if user_input == 1:
            open_account()
            break
            
        elif user_input == 2:
            deposit_amount()
            break
        
        elif user_input == 3:
            withdraw_amount()
            break
        
        elif user_input == 4:
            check_balance()
            break
        
        elif user_input == 5:
            transfer_amount()
            break
        
        elif user_input == 6:
            close_account()
            break
        
        elif user_input == 7:
            request_loan()
            break

        elif user_input == 999:
            view_all_accounts()
            break
    except ValueError:
        print(f" !!! Invalid Value !!! ")
        
    