##Tupes are an ordered set of data
#They are immutable => You can't append data to them

t = "a", "b", "C"
print(t)

imelda = "More Mayhem", "Emilda May", 2011

print(imelda)
print(imelda[0])

#But you cant modify them, this wont work!
# imelda[1] = "Imelda May"

#But you can do this(for tuples):
imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

#Lists are mutable
metallica = ["Ride the Lightning", "Metallica", 1984]
print(metallica)
metallica[0] = "Master of Puppets"
print(metallica)

#Why to use tuples: Hashes, dictionaries, also they can handle heterogeneous items

#So we can also do this weird variable assignment(unpacking tuple)
title, artist, year = imelda
print(title)
print(artist)
print(year)
