bal = 3000
password = "123"
q = 1

def balance_Enquiry():
    print("your current account bal is ",bal)
def Withdrwal(bal):
    amt = int(input("enter amount to withdraw"))
    if (bal-amt>1000):
        bal -= amt
        print("you current account bal is ",bal)
    else:
        print("Sorry!!!! Your balance is insufficient")
    return bal
def Deposit(bal):
    amt = int(input("enter amount deposited"))
    bal += amt
    print("you current account bal is ", bal)
    return bal
def Pinchange(password):
    password = input("Enter your new pin")
    print("password setted successfully")
    return password
while(q):
    p = input("enter your password")
    if(p == password):
        print("Welcome to ABC bank")
        option = int(input("please select \n1. Balanace enquiry \n2. Withdrawal    "
                           " \n3. Deposit \n4. Pinchange \n5. quit\n"))
        if(option == 1):
            balance_Enquiry()
        elif(option == 2):
            bal = Withdrwal(bal)
        elif(option == 3):
            bal = Deposit(bal)
        elif(option == 4):
            password = Pinchange(password)
        elif (option == 5):
            q = 0
        else:
            print("Invalid Option")
    else:
        print("Please enter a valid password")