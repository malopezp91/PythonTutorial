##You can have different ranges that are considered the same, such as:
print(range(0,5,2) == range(0,6,2))

##You can go backwards using ranges
for i in range(10,0,-2):
    print (i, end=',')
print("\n")

#Two ways to do the same range, one using a slice and the second one using only range
print(range(0, 10,)[::-2] == range(9,0, -2))

#this wont print anything at all
for i in range(0,100, -2):
    print(i)

#We can use slits to reverse strings
backString = "ko si siht"
print(backString[::-1])

r =range(0, 10)
for i in r[::-1]:
    print(i)

##Challenge:
## Define what is going to be displayed every time:

##This will display only the range object
o = range(0,100,4)
print(o)

##This will print another object
p = o[::5]
print(p)

#This will actually print the list
for i in p:
    print(i)
