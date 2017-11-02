
age = int(input("How old are you? "))


# if (age >= 16) and (age <= 65):
# We can use a cooler way to do this:
if (15 <= age <= 65):
    print("Have a good day at work!")


if(age < 15) or (age > 65):
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# What is false in Python?? the variables that are empty (uninitialized)
x = {}
if x:
    print("The variable is evaluated as true")

# You can use this to make validation from inputs
x = input("Please enter some text:")

if x:
    print("You entered {}".format(x))
else:
    print("You did not enter anything")

# How to negate a value
print(not False)
print(not True)

if not(age < 18):
    print("You can vote!")

#You can use IN to validate if given value is inside another one
# Probably used in arrays or in strings

parrot = "Norwegian Blue"

letter = input("Enter a char:")

if letter in parrot:
    print("Letter {} was found in {}".format(letter, parrot))
else:
    print("Letter was not found")
