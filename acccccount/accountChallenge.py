import ClassforAccounting as ca

Q = input("Enter the account name (acc1 or acc2): ")
if Q == 'acc1':
    acc1 = ca.Account(input("Enter the customer's name: "), int(input("Enter the customer's balance: ")))
    requirement = input('Enter the requirement: ')
    requirement.lower()
    if requirement == 'deposit':
        amount = int(input('Enter the amount of money for deposit: '))
        acc1.deposit(amount)
        print(acc1.__str__())
    if requirement == 'withdrawl':
        amount = int(input('Enter the amount of money for withdrawl: '))
        acc1.withdrawl(amount)
        print(acc1.__str__())

if Q == 'acc2':
    acc2 = ca.Account(input("Enter the customer's name: "), int(input("Enter the customer's balance: ")))
    requirement = input('Enter the requirement: ')
    requirement.lower()
    if requirement == 'deposit':
        amount = int(input('Enter the amount of money for deposit: '))
        acc2.deposit(amount)
        print(acc2.__str__())
    if requirement == 'withdrawl':
        amount = int(input('Enter the amount of money for withdrawl: '))
        acc2.withdrawl(amount)
        print(acc2.__str__())
    

print("Thank you.")
