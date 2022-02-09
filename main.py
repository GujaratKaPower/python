#creating Bank Account      
class Bank_Account:
    #Creating Bank Account
    Account_name = str(input("Enter your Name:-"))
    print("\n Account is Created:", type(Account_name))
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal")
    #For Deposit  
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
    #For Withdrawal
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")
    #For Transfer
    def transfer(self):
        amount= float(input("Enter amount to be transfered: "))
        if self.balance>=amount:
          self.balance-=amount
          print("you Transferred", amount)
        else:
          print("\n Insufficient balance cannot transfer")
    #For Available balance
    def display(self):
        print("\n Net Available Balance=",self.balance)
        print("Want to quit application",quit)
        quit


s = Bank_Account()

s.deposit()
s.withdraw()
s.transfer()
s.display()






