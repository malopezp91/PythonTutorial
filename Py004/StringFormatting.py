age = 24

# This is the only way to work, as it is typed
print("My age is: " + str(age))

print("My age is: {0}".format(age))

print("January {2} February {0} March {2} April{1}".format(28, 30, 31))

# The old way to do it
print("My age is: %d" % age)
print("I am %d %s old" % (age, "years"))

# Number formatting (as in Matlab, for decimals and stuff)
# The new way
for i in range(1, 12):
    print("Number {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print("PI es aprox {0:12.50}".format(22/7))

# The old way
for i in range(1, 12):
    print("Number %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

print("PI is aprox %12.50f" %(22/7))
