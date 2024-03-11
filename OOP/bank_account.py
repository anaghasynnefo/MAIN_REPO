class bankaccount:

    def __init__(self):
        self.balance=0
        print("WELCOME TO  ***SBI TRANSACTIONS***")

 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited  : "))
        self.balance += amount
        print("Amount Deposited :",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn   : "))
        if self.balance>=amount:
            self.balance-=amount
            print("You Withdraw amount of  :", amount)
        else:
            print("Insufficient balance  ")
 
    def display(self):
        print("Available Balance  =",self.balance)

s =bankaccount()
  
s.deposit()
s.withdraw()
s.display()