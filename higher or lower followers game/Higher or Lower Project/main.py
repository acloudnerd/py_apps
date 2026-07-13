from game_data import data
import random
from art import logo, vs

def account_details(account):
    """prints the data in a proper format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f" {account_name}, a {account_description}, from {account_country}"

def check_guess(user_guess, count_a, count_b):
    if count_a > count_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
continue_gaming = True
random_account_b = random.choice(data)

while continue_gaming:
    random_account_a = random_account_b
    random_account_b = random.choice(data)


    if random_account_a == random_account_b:
        random_account_b = random.choice(data)

    print(f"Compare A: {account_details(random_account_a)}")
    print(vs)
    print(f"Against B: {account_details(random_account_b)}")
    guess = input("Who has more followers 'A' or 'B'?   ").lower()

    print("\n" * 10)
    print(logo)


    account_follow_count_a = random_account_a["follower_count"]
    account_follow_count_b = random_account_b["follower_count"]

    is_correct = check_guess(guess, account_follow_count_a, account_follow_count_b)

    if is_correct:
        score += 1
        print(f"You are correct! And your current score is: {score}")
    else:
        print(f"You are wrong! And your final score is: {score}")
        continue_gaming = False



