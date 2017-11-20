fruits = {"orange": "a sweet, orange, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit growing in bunches",
          "lime": "a sour, green citrus fruit"}

# Update method

veg = {"cabbage": "every childs favorite",
       "sprouts": "mmm, lovely!",
       "spinach": "can I have some more fruit"}

print(veg)

#So you can join them
fruits.update(veg)
print(fruits)

#And you can copy the dictionary
newDictionary = fruits.copy()
print(newDictionary)

#Which is completely discoupled from original
fruits.clear()
print(fruits)
print(newDictionary)
