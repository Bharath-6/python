#Encapsulation
#Wrapping data and functions into a single unit(object).
#Practice:
""" create Account class with 2 Attributes - balance & account no.
Create Methods for Debit, Credit & printng the balance."""

#The below code is not example of encapsulation
class Account:
    def __init__(self,bal,ac):
        self.balance = bal
        self.account_no = ac
    def debit(self,ammount):
        self.balance -= ammount
        print("Rs.",ammount,"was debited")
        print("Total balance = ", self.get_balance())

    def credit(self,ammount):
        self.balance +=ammount
        print("Rs.",ammount,"was credited")
        print("Total balance = ", self.get_balance())
    def get_balance(self):
        return self.balance

acc1 = Account(50000,987456321)
acc1.debit(1000)
acc1.credit(2000)
