
#This is how we execute a while loop in Python
#We need to initialize varible
i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

#Another way to do a while loop, is to have an inner way to break the condition from inside
i = 0
while i < 50:
    i += 1
    print("The value of i is: {}".format(i))
    if i == 45:
        break

availableExits = ["east", "north", "south"]

chosenExit = ""
while chosenExit not in availableExits:
    chosenExit = input("Please choose a direction: ")
