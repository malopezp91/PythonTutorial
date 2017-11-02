varaibleOne = "Good"
variableTwo = "Day!"

age = 24
print(age)

# Varaibles of different type can't be added, this is not stupid JS
# print(variableTwo + age)

# Integers
a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
# Returns as a float
print(a / b)
# Returns as an integer
print(a // b)
print(a % b)

print("Now a for loop will be printed")
for i in range(1, 4):
    print(i)

print("Second loop using inner operation")
for i in range(1, a //b):
    print(i)