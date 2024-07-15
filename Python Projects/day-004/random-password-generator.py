import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password Generator")
letter_amount = int(input("How many letters?: "))
symbol_amount = int(input("How many symbols?: "))
number_amount = int(input("How many numbers?: "))

password = []
for number in range (1, letter_amount + 1):
  password += random.choice(letters)

for number in range (1, symbol_amount + 1):
  password += random.choice(symbols)

for number in range (1, number_amount + 1):
  password += random.choice(numbers)

print(password)

newpassword = ""
for number in range(0, len(password)):
  char = random.randint(0, len(password) - 1)
  newpassword += password[char]
  password.pop(char)

print(f"Password: {newpassword}")