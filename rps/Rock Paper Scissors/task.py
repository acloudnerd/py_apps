import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ["rock", "paper", "scissors"]
art = {"rock": rock, "paper": paper, "scissors": scissors}

user = input("Rock, Paper, or Scissors? ").lower()

if user not in choices:
    print("Invalid choice!")
else:
    computer = random.choice(choices)
    print(f"You chose:\n{art[user]}")
    print(f"Computer chose:\n{art[computer]}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")