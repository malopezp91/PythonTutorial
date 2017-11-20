#Are like system dictionaries
#Same awares apply, as in pickle, when unshelving files from uknown sources
import shelve

#Shelves are read/write by nature
with shelve.open("ShelfTest") as fruit:
    fruit["orange"] = "a sweet, orange, citrus fruit"
    fruit["apple"] = "good for making cider"
    fruit["lemon"] = "a sour, yellow citrus fruit"
    fruit["grape"] = "a small, sweet fruit"
    fruit["lime"] = "a sour, green citrus fruit"

    #You can remove items using
    # del fruit["lime"]

    print(fruit["lemon"])
    print(fruit["grape"])


#Everytime you write to the file, the information stays.
#SO it may happen that you can retrieve data that you didn't know it was there
