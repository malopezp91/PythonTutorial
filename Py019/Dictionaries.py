# Dictionaries and Sets are unordered collections
# Both guarantee that there won't be any duplicate items
# You can access individual items using an index

# Dictionaries are key-value pairs
fruits = {"orange": "a sweet, orange, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit growing in bunches",
          "lime": "a sour, green citrus fruit"}

print(fruits)
print(fruits["grape"])

# We can add a new item to dictonary
fruits["pear"] = "an odd shaped fruit"
print(fruits)

#If we add another entry with same key, the value is overwritten
fruits["lime"] = "great with tequila"
print(fruits)

#We can delete items
del fruits["lemon"]
print(fruits)

#This will delete the entire dictionary
# del fruits
# print(fruits)

#But we can clear it
fruits.clear()
print(fruits)
fruits = {"orange": "a sweet, orange, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit growing in bunches",
          "lime": "a sour, green citrus fruit"}

#We can validate a key exists in dictionary by:
print("lemon" in fruits)

#And we can retrieve safely the value using:
print(fruits.get("lemon"))
print(fruits.get("lem"))
