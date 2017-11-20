#Write into a file and read it back again some binary data
#We need to specify we are writing binary data
#Strings and Integers cannot be written to a file directly, have to be converted
#to a Byte

with open("binary", "bw") as binFile:
    for i in range(17):
        binFile.write(bytes([i]))
#Bytes needs a list, in which the integer is found

#Now read it
with open("binary", "br") as binFile2:
    for b in binFile2:
        print(b)