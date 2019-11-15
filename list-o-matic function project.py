myList = ["human", "cat", "bird", "dog", "elephant", "lion"]
print("Here is the list: " + str(myList))

def list_o_matic(animal):
    if animal == "":
        animal = myList.pop()
        print(animal.lower() + " has popped from the list.")
    elif animal.lower() in myList:
        print(animal.lower() + " has gone!")
        return myList.remove(animal)
    else:
        print("1 instance of " + animal.lower() + " has appended to the list")
        return myList.append(animal)

while myList:
    animal = input("Enter any type of animal or 'QUIT' to quit: ")
    if animal.upper() == "QUIT":
        print("Good Bye.")
        break
    else:
        print("This is the new list: " + str(myList))
        list_o_matic(animal)
        print(myList)

print("The list is empty. Good Bye.")
        
