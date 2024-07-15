print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right": ').lower()

if choice1 == "left":
  choice2 = input("Swim or wait?: ").lower()
  if choice2 == "wait":
    choice3 = input("Which door? Red, blue, or yellow?: ").lower()
    if choice3 == "yellow":
      print("You win.")
    elif choice3 == "red":
      print("Deaded.")
    elif choice3 == "blue":
      print("Deadedest.")
    else:
      print("Dead.")
  else:
    print("Dead.")
else:
  print("Dead.")