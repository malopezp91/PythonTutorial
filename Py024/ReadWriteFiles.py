
#This is one way to open the file and use it, beware of closing
jabber = open("./sample.txt")

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()

#Another way to it, using "With" and an alias
print()
with open("./sample.txt") as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

#We can also use, readLines that return all as a Sequence

#read() reads all the data
#readline() reads upto the newline
#readlines() reads everything and returns a list with all lines