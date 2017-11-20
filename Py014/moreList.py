list1 = []
list2 = list()

print("List1: {}".format(list1))
print("List2: {}".format(list2))

if list1 == list2:
    print("The lists are equal")

print(list("This lists are equals"))

#So python passes as reference...
even = [2, 4, 6, 8]

anotherEven = even
anotherEven.sort(reverse=True)
print(even)
print(anotherEven is even)

yetAnotherList = list(even)
print(yetAnotherList)
print(yetAnotherList is even)

## So..
## == is used to compare the contents 
## is is used to compare the pointers (reference variable )

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

listOne = even + odd
print(listOne)

listTwo = [even, odd]
print(listTwo)

for numberSet in listTwo:
    print(numberSet)

    for value in numberSet:
        print(value)
