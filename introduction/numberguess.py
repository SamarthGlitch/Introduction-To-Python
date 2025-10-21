import random

number = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    else:
        print("Correct! You win.")
        break
