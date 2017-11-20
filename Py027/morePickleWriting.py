import pickle

even = list(range(2, 10, 2))
odd = list(range(1, 10, 2))

#We can write any kind of data easily
with open("variables.pickle", "wb") as writingFile:
    pickle.dump(even, writingFile)
    pickle.dump(odd, writingFile)
    pickle.dump(2998302, writingFile)

#We need to retrieve the data in the same order
with open("variables.pickle", "rb") as readingFile:
    evenAsList = pickle.load(readingFile)
    oddAsList = pickle.load(readingFile)
    x = pickle.load(readingFile)

#Now we can print the retieved values
print(evenAsList)
print(oddAsList)
print(x)

#This way is easier than converting everything to binaries and then save them
#There are few objects in Python that can't be saved by pickle
#You can use one of 5 different protocols for serialization
#Protocols arent backward compatible
