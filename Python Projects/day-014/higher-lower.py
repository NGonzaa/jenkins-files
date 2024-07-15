import art # "logo" has the game logo, "vs" has the vs logo that goes between each person/thing being compared.
from game_data import data # "data" is a list of dictionaries, each dictionary has a person/thing and related data.
import random

score = 0
person_1 = {}
person_2 = {}

def choices(person_1, person_2, score):
    if score == 0:
        person_1 = random.choice(data)
        data.remove(person_1)
        person_2 = random.choice(data)
        data.remove(person_2)
    elif person_1 == {}:
        person_1 = person_2
        person_2 = random.choice(data)
        data.remove(person_2)
    elif person_2 == {}:
        person_2 = random.choice(data)
        data.remove(person_2)
    print(f"{person_1['name']}, a {person_1['description']} from {person_1['country']}.")
    print(art.vs)
    print(f"{person_2['name']}, a {person_2['description']} from {person_2['country']}.")
    return person_1, person_2, person_1['follower_count'], person_2['follower_count']

continue_playing = True
print(art.logo)
while continue_playing == True:
    followers = choices(person_1, person_2, score)
    person_1 = followers[0]
    person_2 = followers[1]
    followers_1 = followers[2]
    followers_2 = followers[3]

    user_guess = int(input("1 or 2?: "))
    if user_guess == 1:
        if followers_1 > followers_2:
            score += 1
            print(f"Correct! Score: {score}")
            person_2 = {}
        else:
            print(f"Incorrect. Final score: {score}")
            continue_playing = False
    elif user_guess == 2:
        if followers_2 > followers_1:
            score += 1
            print(f"Correct! Score: {score}")
            person_1 = {}
        else:
            print(f"Incorrect. Final score: {score}")
            continue_playing = False
    print("------------------")