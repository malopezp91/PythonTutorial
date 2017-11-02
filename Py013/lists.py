
ipAddress = input("Please enter an IP address: ")
print(ipAddress.count("."))

parrotList = ["non pinin", "no more", "a stiff", "bereft of live"]
parrotList.append("A Norwegian Blue")

for state in parrotList:
    print("This parrot is: " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers.sort()

#This wont work!
print(numbers.sort())
#This will work
print(numbers)
#Also this
print(sorted(numbers))

numbers = even + odd
numbersInOrder = sorted(numbers)

if numbers == numbersInOrder:
    print("The list are equal")
else:
    print("The lists are not equal")

if numbersInOrder == sorted(numbers):
    print("The list are equal")
else:
    print("The lists are not equal")
