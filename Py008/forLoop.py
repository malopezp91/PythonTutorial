
# In for loops, first values is included but last value is not included
for i in range(1, 20):
    print("i is now {}".format(i))

# In Python, you dont need to do the lenght - 1 stuff
number = "9,222,372,036,854,777"
print("Iterate through number")
for i in range(0, len(number)):
    print(number[i],end='')

# Print only the numbers without the commas
number = "9,222,372,036,854,777"
print("\n Iterate through number removing commas")
for i in range(0, len(number)):
    if number[i] in "0123456789":
        print(number[i], end='')
