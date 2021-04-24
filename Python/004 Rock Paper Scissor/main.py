import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))

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


if user_choice == 0:
	print(rock)
elif user_choice == 1:
	print(paper)
else:
	print(scissors)


print("Computer chose:")
computer_choice = random.randint(0, 2)

if computer_choice == 0:
	print(rock)
elif computer_choice == 1:
	print(paper)
else:
	print(scissors)


win = ["02", "10", "31"]
lose = ["01", "12", "20"]

versus = f"{user_choice}{computer_choice}"

if versus in win:
	print("You Win")
elif versus in lose:
	print("You Lose")
else:
	print("You Draw")
