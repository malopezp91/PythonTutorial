# This will only print the range object
print(range(10))

# This will print all items in the list
listOne = list(range(10))
print(listOne)

even = list(range(0, 100, 2))
odd = list(range(1, 100, 2))
print(even)
print(odd)

#Using index access
myString = "abcdefg"
print(myString.index("e"))
print(myString[4])

print(listOne.index(3))

#Access a value in odd list
print(odd[30])

sevens = range(7,100000, 7)
x = int(input("Please enter a positive number "))

if (x in sevens):
    print("{} is divisible by seven".format(x))

#We can extract values inside a range using brackets and ::
decimals = range(100)
myRange = decimals[::2]

for i in myRange:
    print(i, end=', ')
