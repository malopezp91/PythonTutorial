import random

highest  = 10
answer = random.randint(1,highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Print guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done!")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time!")
