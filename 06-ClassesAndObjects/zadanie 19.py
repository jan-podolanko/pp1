class bank_account():
    def __init__(self, account_no):
        self.account_no = account_no
        self.balance = 0.0
    def deposit(self, a):
        self.balance += a
    def withdraw(self, b):
        if b <= self.balance:
            self.balance -= b
            print(f'{round(b,2)}$ withdrawn')
        else:
            print('Insufficient funds to withdraw')
    def account_status(self):
        print(f'Account number: {self.account_no}')
        print(f'Balance: {round(self.balance,2)} $')

x = bank_account('12 3456 5555 9090 1111 0000 7722')
x.account_status()
x.deposit(25)
x.account_status()
x.withdraw(12.55)
x.account_status()
x.withdraw(100)
x.account_status()