fruits = {"orange": "a sweet, orange, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit growing in bunches",
          "lime": "a sour, green citrus fruit"}

##Iteractive way to display the contents of dictionary

# while True:
#     inputKey = input("Please enter a key: ")
#     if inputKey == "quit":
#         break
#     if inputKey in fruits:
#         print(fruits.get(inputKey))
#     else:
#         print("We don't have that key in the dictionary")

#No guarantee items will be printed in the same order
for snack in fruits:
    print(fruits[snack])

#We can sort the keys, but we need to create a list
orderedKeys = list(fruits.keys())
orderedKeys.sort()
print("")
for fruitKey in orderedKeys:
    print("{} - {}".format(fruitKey, fruits[fruitKey]))

#You can get a reference to keys and value object.
keyValues = fruits.keys()
valueValues = fruits.values()

fruits["tomato"] = "Not nice with icecream"

#Now tomato will be included
print(keyValues)
