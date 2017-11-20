#Similar to a dictionary, but items arent accessed by a key
farmAnimals = {"sheep", "cow", "hen"}
print(farmAnimals)

wildAnimals = set(["lion", "tiger", "panther"])
print(wildAnimals)

#Sets are unordered
farmAnimals.add("horse")
wildAnimals.add("elephant")
print(farmAnimals)

#How to create a set from a range and a tuple
even = set(range(0, 40, 2))
print(even)
squaresAsTuple = (4, 9, 16, 25)
squares = set(squaresAsTuple)
print(squares)

#You can do a union between sets (Notice even is not modified)
print(even.union(squares))

#You can do the intersections (also you can use & symbol)
print(even.intersection(squares))

#You can also do difference or substraction (also using symbol -)
print(even.difference(squares))

#You can affect the original set by using difference_update
even.difference_update(squares)
print(even)
even = set(range(0, 40, 2)) #Regenerate even variable

#Also do a symmetric difference (items in either of the sets but not in intersection)
print(even.symmetric_difference(squares))

#Discard wont trow an error if element does not exist
squares.discard(4)
squares.discard(5)
print(squares)

#Remove will throw an error
squares.remove(9)
print(squares)

#You can validate item existst in set or also to catch exception
try:
    squares.remove(8)
except KeyError:
    print("Item 8 is not part of the set")

squaresAsTuple = (4, 16)
squares = set(squaresAsTuple)

#We can test for subsets and supersets
if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is superpset of squares")

#Frozen set is an immutable set
even = frozenset(range(0, 100, 2))

print(even)