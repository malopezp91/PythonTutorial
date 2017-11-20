#Using default iterator for a String
#Iterator is created from the string
#The for loop uses it to return each item of the string
#At the end, iterator returns and error but it is handled by the for loop
string = "1234567890"
for char in string:
    print(char)

#We can call the iterator manually
myIterator = iter(string)
print(myIterator)
print(next(myIterator))
print(next(myIterator))
#If we continue, we will get an error for position 11

#so the first code is the same to the following:
for char in iter(string):
    print(char)

challengeList  = ["monday", "tuesday", "wednesday", "thursday", "friday"]
challengeIterator = iter(challengeList)
for i in range(0, len(challengeList)):
    print("Challenge Iterator: " + next(challengeIterator))