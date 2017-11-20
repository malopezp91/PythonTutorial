with open("sample.txt", "a") as poemFile:
    for i in range(1,12):    
        print("{:2} times 2 is {:2}".format(i, i * 2), file=poemFile)