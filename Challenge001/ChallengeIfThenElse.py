#Write a small program to ask for a name and an age
#When both values have been entered, check if the person 
# is the right age to go on a 18-30 holiday 
#If they, welcome them to the holiday, otherwwise print a 8polite)
#message refusing them entry
print("Challenge 1: If-Then-Else")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if name and age:
    if (age >= 18 ) and (age <= 30):
        print("Welcome to the holiday")
    else:
        print("Sorry, you can't come to the holiday")
else:
    print("Data was empty")