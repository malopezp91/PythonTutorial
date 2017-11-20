fruits = {"orange": "a sweet, orange, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit growing in bunches",
          "lime": "a sour, green citrus fruit"}

#We can use items to access the dictionary
print(fruits.items())

#So we can create a tuple based on the dictionary
fruitsAsATuple = tuple(fruits.items())

print(fruitsAsATuple)
