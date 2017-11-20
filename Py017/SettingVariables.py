#Different ways to set valued to variables
a = b = c = d = 12
a, b = 12, 13
print(a, b, c, d)

a, b  = b, a
print("a is {} and b is {}".format(a, b))
