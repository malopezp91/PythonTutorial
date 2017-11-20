# Create a program that takes some test
# and returns a list of all the characters in the text that are not vowels,
# sorted in alphabetical order

vowels = frozenset("aeiou ")
print(vowels)

stringToTest = "Hello World"

finalSet = set(stringToTest).difference(vowels)
print(sorted(finalSet)) 