#You need to modify the program used for guessing game to allow as many guesses 
# as necessary

#The program should let the player know wheter to guess higher or lower,
#and should print the message when the guess is correct. A correct guess
#will terminate the program

#As an optional extra, allow the player to quit by entering zero for their guess

import random

highest  = 10
answer = random.randint(1,highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())

while guess != answer:
    if guess == 0:
        break
    elif guess < answer:
        print("Please guess higher")
    else:
        print("Print guess lower")
    guess = int(input())
else:
    print("You got it!")

