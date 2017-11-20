#This will print some system/Python variables that start with _
#As there are no private variables, the underscore means you shouldnt change that stuff

#dir() has to do with internal stuff of Python
#Check the built-in Functions
# Always available and no need of import
print(dir())
for m in dir(__builtins__):
    print(m)