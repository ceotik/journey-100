import random

print("Welcome to the Number Guessing Game!")

secret = random.randint(1, 20)   # computer picks a number
attempts = 0
guess = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"🎉 Correct! The number was {secret}. It took you {attempts} attempts.")