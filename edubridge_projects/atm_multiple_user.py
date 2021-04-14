import sys
account_details = {
                   123:{"password":1234,"Name":"Sethu","Balance":1000},
                   456:{"password":2345,"Name":"Akshara","Balance":2000},
                   789:{"password":4576,"Name":"Sandeep","Balance":3000},
                   147:{"password":5678,"Name":"Sabu","Balance":4000},
                   258:{"password":6789,"Name":"Sushama","Balance":5000},
                   369:{"password":7890,"Name":"Seetha","Balance":6000},
                   159:{"password":8901,"Name":"Malu","Balance":7000}
                   }
def Withdrawal(A_N):
    amt = int(input("Enter the amount to withdraw"))
    if account_details[A_N]["Balance"]-amt>1000:
        account_details[A_N]["Balance"] -= amt
        print("Amount withdrawn successfully...\n Your Account balance is ",account_details[A_N]["Balance"])
    else:
        print("You have insufficient balance")
def Deposit(A_N):
    amt = int(input("Enter the amount to Deposit"))
    account_details[A_N]["Balance"] += amt
    print("Cash received Successfully...\n Your Account balance is ", account_details[A_N]["Balance"])
def Checkbalance(A_N):
    print("Your available balance is",account_details[A_N]["Balance"])
def Reset_password(A_N):
    new_pw = int(input("Enter the new password"))
    account_details[A_N]["password"] = new_pw
    print("password updated successfully")
while(1):
    print("!!!Welcome To ABC Bank!!!!\n")
    Acnt_N = int(input("Enter your account Number"))
    PW = int(input("Enter password"))
    if Acnt_N in account_details and account_details[Acnt_N]["password"] == PW:
        print("...",account_details[Acnt_N]["Name"])
        option = int(input("!!!Welcome {0} !!!!\nPlease Enter \n"
                           "1. Check balance\n2. Deposit\n3. Withdrawal\n"
                           "4.Reset Password\n5. Exit".format(account_details[Acnt_N]["Name"])))
        if option == 1:
            Checkbalance(Acnt_N)
        elif option == 2:
            Deposit(Acnt_N)
        elif option == 3:
            Withdrawal(Acnt_N)
        elif option == 4:
            Reset_password(Acnt_N)
        elif option == 5:
            sys.exit()
        else:
            print("Invalid Option")
    else:
        print("Sorry...\nAccount number or password Entered is incorrect......\n"
              "!!!!!!!!!!Try Again!!!!!!!")

