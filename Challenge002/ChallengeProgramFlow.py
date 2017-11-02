# Create a program that takes an IP address entered at the keyword
# and prints out the number of segments if contains, and the length of each segment

# An IP address consist of 4 numbers, separated from each other with a full stop.
# But your program should just count however many are entered. 
# Examples are: 
# 127.0.0.1
#.192.168.0.1
#10.0.14526.255
#172.52

# So your program should work even with an invalid IP address. We're just interested in the 
# number of segments and how long each one is

ipAddress = input("Please enter an IP address:")

segment = ""
for char in ipAddress:
    if char == ".":
        print("Segment is {} with size {}".format(segment, len(segment)))
        segment = ""
        continue
    segment += char
print("Segment is {} with size {}".format(segment, len(segment)))

