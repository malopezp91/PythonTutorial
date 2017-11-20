# Refers to serialization, as Java
# Mechanism called Pickle
import pickle

imelda = ("More Mayhem", "Imelda May", 2011,
          ((1, "Pulling the Rug"),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentish Town Waltz")
           ))

#We can write easily
with open("imelda.pickle", "wb") as pickleFile:
    pickle.dump(imelda, pickleFile)

#Now lets read
with open("imelda.pickle", "rb") as imeldaPickled:
    imeldaRetrieved = pickle.load(imeldaPickled)

print(imeldaRetrieved)

album, artist, year, tracks = imeldaRetrieved

print(album)
print(artist)
print(year)
for track in tracks:
    trackNumber, trackTitle = track
    print(trackNumber, trackTitle)
