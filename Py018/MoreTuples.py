
#IF you try to unpack a list/tuple that contains more or less items than expected, an error is thrown
metallica = ["Ride the Lightning", "Metallica", 1984]

#This won't throw an error
title, artist, year = metallica

# but this will:
# title, artist = metallica

#So we can use tuples so this won't happen, as tuples are immutable

#You can have tuple inside a tuple
imelda = "More Mayhem", "Imilda May", 2011,(
    (1, "Pulling the Rug"), (2, "Psyicho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

print(imelda)

#Do some unpacking
title, artist, year, tracks = imelda
print(title)
print(artist)
print(artist)
print(tracks)

trackOne, trackTwo, trackThree, trackFour = tracks
print(trackOne)
