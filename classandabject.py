class BankAccount():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance


    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient funds"

        else:
            self.balance = self.balance - amount
            return self.balance


    def show_balance(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"



acc = BankAccount("Nisanth",1240)

print(acc.show_balance())