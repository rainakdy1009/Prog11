import ClassforAccounting as ca

acc1 = ca.Account('Jose', 100)
acc2 = ca.Account('Zelda', 500)

acc1.deposit (200)
acc1.withdrawl(700)
acc2.deposit(200)
acc2.withdrawl(700)

print(acc1.owner, acc1.balance)
print(acc2.owner, acc2.balance)
acc1.deposit(20.23*1.22)
print(acc1.__str__())
print(acc2.__str__())
