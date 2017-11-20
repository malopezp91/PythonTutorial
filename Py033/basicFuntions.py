#Functions! At last!

def pythonFood():
    width = 50
    text = "Spam and eggs"
    leftMargin = (width - len(text)) // 2
    print(" " * leftMargin, text)

def centreText(*args, sep = " "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    leftMargin = (80 - len(text)) // 2
    print(" " * leftMargin, text)

def finalFunction(arg1, arg2):
    var1 = arg1 + arg2
    var2 = arg1 * arg2
    return var1, var2
    
#Call the function
pythonFood()
centreText("Spam and Eggs!")
centreText("Spam, spam, spam and Eggs!")
centreText("Spam", "Spam", "Bacon")

#We can parse now use numbers, due of line 10
#Also, we can pass the value for sep to overwrite the default sep
centreText(89, 94, 47, sep = ",")

#You can also create a function that returns several values
#LEft sided values need to match the returned values, or only be one; otherwise unpacking fails
a, b  = finalFunction(4, 5)
print(a, b)

#If function returns several values, and number of left sided variables do not match the returned values
#Left sided variable contains all returned responses
a = finalFunction(4, 5)
print(a)

# #If return is not defined, it will return 'None'
# print(pythonFood())

#If you declare a function with (*args), this param can be as many as you want

#You can set defualt param values with (stuff = 7)