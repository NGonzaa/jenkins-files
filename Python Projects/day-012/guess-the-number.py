from random import randint
from art import logo

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

def set_difficulty():
    difficulty = input("Choose easy or hard difficulty: ").lower()
    if difficulty == "easy":
        return EASY_DIFFICULTY
    else:
        return HARD_DIFFICULTY

def check(number, turns):
    while turns > 0:
        guess = int(input("Choose a number between 1 and 100: "))
        while not 0 < guess < 101:
            guess = int(input("Between 1 and 100!: "))
        if guess == number:
            print(f"Correct! The answer is {number}.")
            break
        elif guess > number:
            print("Too high.")
            turns -= 1
        elif guess < number:
            print("Too low.")
            turns -= 1
        if turns == 0:
            print("You lose.")

def play_game():
    print(logo)
    number = randint(1, 100)
    print(number)
    turns = set_difficulty()
    check(number, turns)

play_game()