import random
from art import logo

# Function setup
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "Dealer has Blackjack, you lose."
    elif player_score == 0:
        return "You have Blackjack, you win."
    elif player_score > 21:
        return "You Bust. You lose."
    elif computer_score > 21:
        return "The dealer Busts. You win."
    elif player_score > computer_score:
        return "You win."
    else:
        return "The dealer wins. You lose."

def play_game():
    print(logo)

    # Starting variables
    player_hand = []
    computer_hand = []
    continue_game = True

    # Initial deal
    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    # Player's turn
    while continue_game:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your hand: {player_hand}, your score: {player_score}.")
        print(f"Dealer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            continue_game = False
        else:
            if input("Do you want another card? y or n: ") == "y":
                player_hand.append(deal_card())
            else:
                continue_game = False

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    # Check hands and compare scores
    print(f"Your hand: {player_hand}, your score: {player_score}.")
    print(f"Dealer's hand: {computer_hand}, dealer's score: {computer_score}.")
    print(compare(player_score, computer_score))

# Game start
while input("Do you want to play Blackjack? y or n: ") == "y":
    play_game()