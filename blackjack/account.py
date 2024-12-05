import time
import pandas as pd


class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = pd.DataFrame(columns=['category', 'amount'])

    def __str__(self):
        return f"Account Owner: {self.owner}\nCurrent Balance: $ {self.balance}"
    
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            return "Transaction must be a number; deposit failed."

        self.dep = pd.DataFrame({
            'category': ['Deposit'],
            'amount': [amount]
        }, index=[0])
        self.transactions = pd.concat([self.transactions, self.dep], ignore_index=True)
        self.balance += amount
        print('Deposit accepted...')
        time.sleep(1)
        print(f"Current Balance $ {self.balance}")
    
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            return "Transaction must be a number; withdraw failed."
        elif amount > self.balance:
            return f"Withdrawal amount greater than available balance ($ {self.balance})."

        self.wth = pd.DataFrame({
            'category': ['Withdraw'],
            'amount': [-amount]
        }, index=[0])
        self.transactions = pd.concat([self.transactions, self.wth], ignore_index=True)
        self.balance -= amount
        print('Withdrawal accepted...')
        time.sleep(1)
        print(f"Current Balance $ {self.balance}")

    def get_transactions(self):
        return self.transactions
    
    def get_balance(self):
        return f"$ {self.balance}"