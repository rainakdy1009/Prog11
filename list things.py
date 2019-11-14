import random

how_many = int(input("Enter how many numbers to add into the list."))
operation = input("Enter an operation: A for addition or M for muliplication.")
count = 0
total = 0
sum1=0
result =1

if operation == "a" or operation == "A":
    for num in range(0, how_many):
         num = random.randint(1, 9)
         print(num)
         sum1 += num
         
    print(sum1)
if operation == "m" or operation == "M":
     for num in range(0, how_many):
         num = random.randint(1, 9)
         print(num)
         result *= num
     print(result)
