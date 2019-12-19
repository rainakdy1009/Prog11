class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:  {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self,dep_amt):
        self.balance +=dep_amt
        print('Deposit Accepted')

    def withdrawl(self, wd_amt):
        if wd_amt < self.balance:
            self.balance -= wd_amt
            print('Withdrawl Accepted -- Thank you: ', self.owner)

        elif wd_amt == self.balance:
            self.balance -= wd_amt
            print("Account Closed -- Thank you:" , self.owner)

        else:
            print('Funds Unavailable--check your math:', self.owner)
            
