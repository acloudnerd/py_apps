import random
from art import logo

print(logo)

print("Let's play a number guessing game.\n")
print("I'm thinking of a number between 1 and 100.\n")

number = random.randint(1, 100)

mode = input("Easy or hard? ").lower()
attempts = 10 if mode == 'easy' else 5
print(f"You have {attempts} attempts. Good luck!\n")

while attempts > 0:
    guess = int(input("Guess the number: "))
    attempts -= 1

    if guess == number:
        print("You got it! 🎉")
        break
    elif guess > number:
        if abs(guess - number) < 10:
            print("Too close, but too high!")
        else:
            print("Too high!")
    elif guess < number:
        if abs(guess - number) < 10:
            print("Too close, but too low!")
        else:
            print("Too low!")

    if attempts > 0:
        print(f"{attempts} attempt(s) remaining.\n")
    else:
        print(f"Out of attempts! The number was {number}.")