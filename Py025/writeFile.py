cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("cities.txt", "w") as citiesFile:
    for city in cities:
        print(city, file=citiesFile)
#Closing the file flushes everything automatically
#This will print all data into the file, separated by newlines


imelda = "More Mayhem", "Imilda May", 2011,(
    (1, "Pulling the Rug"), (2, "Psyicho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

#This will print the tuple as a string
#Data can be read using eval to return string as a tuple
with open("imelda.txt", "w") as imeldaFile:
    print(imelda, file=imeldaFile)

#Now we can retrieve the data
with open("imelda.txt", "r") as imeldaFile:
    contents = imeldaFile.readline()

readImelda = eval(contents)

print(readImelda)
title, artist, year, tracks= readImelda
print(title)
print(artist)
print(year)

