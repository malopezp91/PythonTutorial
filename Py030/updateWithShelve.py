import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beansOnToast = ["beans", "bread"]
scrambledEggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

#If we execute this code first, and then we comment the other code, the file will be updated


#The other way to always write the changes into the file, is with:
# with shelve.open("recipes", writeback=True) as recipes:

with shelve.open("recipes") as recipes:
    # recipes["blt"] = blt
    # recipes["beansOnToast"] = beansOnToast
    # recipes["scrambledEggs"] = scrambledEggs
    # recipes["pasta"] = pasta
    recipes["soup"] = soup

    #If we try to append data, this won't be reflected into file
    #This is because we have good I/O performance, no unnecesarry writes
    # recipes["blt"].append("butter")

    #So we can do the following to update:
    tempVar = recipes["blt"]
    tempVar.append("butter")
    recipes["blt"] = tempVar

    for snack in recipes:
        print(snack, recipes[snack])
