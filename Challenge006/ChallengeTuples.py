#You have to pretty print the following tuples

imelda = "More Mayhem", "Imilda May", 2011,(
    (1, "Pulling the Rug"), (2, "Psyicho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

title, artist, year, tracks = imelda

print("Album: {}, Artist: {}, Year: {}".format(title, artist, year))
for track in tracks:
    number, song = track
    print("\t Track number {}, Title: {}".format(number, song))

#If a tuple contains a list, this list can be modifed and new items can be appended