import sys

class bank:
    balance = 0
    pass_word = ""
    def balance_enquiry(self):
        print("your current account bal is ",self.balance)
    def withdrwal(self):
        amt = int(input("enter amount to withdraw"))
        if (self.balance-amt>1000):
            self.balance -= amt
            print("you current account bal is ",self.balance)
        else:
            print("Sorry!!!! Your balance is insufficient")

    def deposit(self):
        amt = int(input("enter amount deposited"))
        self.balance += amt
        print("you current account bal is ", self.balance)

    def pinchange(self):
        self.pass_word = input("Enter your new pin")
        print("password setted successfully")
customer = bank()
customer.balance = 3000
customer.pass_word = "123"
while(1):
    p = input("enter your password")

    if p == customer.pass_word:
        print("Welcome to ABC bank")
        option = int(input("please select \n1. Balanace enquiry \n2. Withdrawal    "
                           " \n3. Deposit \n4. Pinchange \n5. quit\n"))
        if option == 1:
            customer.balance_enquiry()
        elif option == 2:
            customer.withdrwal()
        elif option == 3:
            customer.deposit()
        elif option == 4:
            customer.pinchange()
        elif option == 5:
            sys.exit()
        else:
            print("Invalid Option")
    else:
        print("Please enter a valid password")