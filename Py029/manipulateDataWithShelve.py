#As always, we import Shelve but we are going to analyze the results and how
#we write and read stuff
import shelve

#Shelves are read/write by nature
with shelve.open("ShelfTest") as fruit:
    fruit["orange"] = "a sweet, orange, citrus fruit"
    fruit["apple"] = "good for making cider"
    fruit["lemon"] = "a sour, yellow citrus fruit"
    fruit["grape"] = "a small, sweet fruit"
    fruit["lime"] = "a sour, green citrus fruit"

    #So if we print the values from the file:
    #They won't be displayed in alphabetical order
    for snack in fruit:
        print(snack + " : " + fruit[snack])

    #If you need to return the keys sorted, you have to sort them manually

#Main difference between shelve and dictinaries:
#Shelve can only have strings as Keys
#Dictionaries can have any object as Keys