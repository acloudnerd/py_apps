import random
import art


def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)

    return random_card

def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lost bc the opponent has blackjack"
    elif user_score == 0:
        return "You won with blackjack!"
    elif user_score > 21:
        return "You went over, so you lost"
    elif computer_score > 21:
        return "Opponent went over, you won!"
    elif user_score > computer_score:
        return "You won"
    else:
        return "You lost"

def play_game():
        print(art.logo)
        user_cards = []
        computer_cards = []
        is_game_over = False
        comp_score = -1
        usr_score = -1

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            usr_score = calculate_score(user_cards)
            comp_score = calculate_score(computer_cards)
            print(f"User cards: {user_cards}, current user score: {usr_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if usr_score == 0 or comp_score == 0 or usr_score > 21:
                is_game_over = True
            else:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass:   ")
                if user_should_deal == 'y':
                    user_cards.append(deal_card())
                else:
                    is_game_over = True
        while comp_score != 0 and comp_score < 17:
            computer_cards.append(deal_card())
            comp_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {usr_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {comp_score}")
        print(compare(usr_score, comp_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n':") == 'y':
    print("\n" * 10)
    play_game()







