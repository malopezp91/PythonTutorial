# First we are using continue so we don't print SPAM
shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shoppingList:
    if item == "spam":
        continue
    print("Buy {}".format(item))

# Then we are using break, so we print up to SPAM
meal = ["egg", "bacon", "spam", "sausages"]

nastyFood = ""
for item in meal:
    if item == "spam":
        nastyFood = item
        break
else:
    print("Else statement is only executed if BREAK was NOT executed")

if nastyFood:
    print("Can't have anything without spam in it")
