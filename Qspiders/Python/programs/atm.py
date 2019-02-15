withdrawal=int(input("enter the amount to be withdrawn "))
atm_balance=200
user_account_balance = 180
if withdrawal<100:
    print("invalid amount entered please enter amount in multiple of 100")
elif withdrawal<atm_balance and withdrawal<user_account_balance:
    atm_balance-=withdrawal
    current_balance= user_account_balance-withdrawal
    print("you have successfully withdrawn "+str(withdrawal)+" and user current balance is "+str(current_balance))
elif withdrawal>atm_balance or withdrawal>user_account_balance:
    if withdrawal>atm_balance:
        print("no sufficent funds available")
    else:
        print("withdrawal amount is greater than amount in your account")
else:
    print("atm is out of service")
