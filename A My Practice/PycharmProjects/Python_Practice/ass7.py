class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:{self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print(f'${dep_amt} Deposit Accepted')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print(f'${wd_amt} Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


acct1 = Account('Shri',800)
print(acct1)
acct1.deposit(200)
acct1.withdraw(500)
print(f'Current balance :{acct1.balance}')