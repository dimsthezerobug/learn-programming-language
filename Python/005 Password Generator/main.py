#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


n_letters = len(letters) - 1
n_numbers = len(numbers) -1
n_symbols = len(symbols) - 1


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print("\nEazy Level")

for _ in range(nr_letters):
	i = random.randint(0, n_letters)
	print(letters[i], end = "")

for _ in range(nr_symbols):
	i = random.randint(0, n_symbols)
	print(symbols[i], end = "")

for _ in range(nr_numbers):
	i = random.randint(0, n_numbers)
	print(numbers[i], end = "")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print("\n\nHard Level")

result = []

for _ in range(nr_letters):
	i = random.randint(0, n_letters)
	result.append(letters[i])

for _ in range(nr_symbols):
	i = random.randint(0, n_symbols)
	result.append(symbols[i])
for _ in range(nr_numbers):
	i = random.randint(0, n_numbers)
	result.append(numbers[i])

randomised_result = []

for x in result:
	i = random.randint(0, len(randomised_result))
	randomised_result.insert(i, x)

for x in randomised_result:
	print(x, end = "")
