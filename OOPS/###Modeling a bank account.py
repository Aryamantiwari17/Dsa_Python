###Modeling a bank account
##define a class for bank account

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} this is the  deposit amount and this {self.balance} is the balance")
        print(f"Thank You {self.owner}")


    def withdrwal(self,amount):
        if amount>self.balance:
            print("No avaible of cash in the account")
        else:
            self.balance-=amount
            print(f"{amount} this is the  withdrawl amount and this {self.balance} is the balance left")
            print(f"Thank You {self.owner}")

    def Get_balance(self):
        print(f"{self.balance} is the balance")
        print(f"Thank You {self.owner}")



customer_1=BankAccount("Aryaman",1000)
customer_1.deposit(100)
customer_1.withdrwal(500)
customer_1.Get_balance()








