import art
import random

def play(difficulty):
    if difficulty == "hard":
        attemp = 5
    elif difficulty == "easy":
        attemp = 10
    

    for _ in range(attemp):
        guess = int(input(f"You have {attemp} attemps remaining to guess the number.\nMake a guess: "))

        if guess == ANSWER:
            return f"You've got it! The answer was {ANSWER}"
        elif guess < ANSWER:
            print("Too low.")
        elif guess > ANSWER:
            print("Too high")

        print("Guess again.")
        attemp -= 1
    return "You've run out of guesses, you lose."


ANSWER = random.randint(0, 100)

print(art.logo)
print("Welcome to the Number Guessing Game !")
print("I'm thinking of number between 1 and 100.")

# # tester code
# print(f"The answer is {ANSWER}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

print(play(level))
