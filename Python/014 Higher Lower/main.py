import art
import game_data
import random
import replit

DATA = game_data.data
# key : name, follower_count, description, country
N_DATA = len(DATA)


def data_generator():
    """return dictionary in list DATA"""

    i = random.randint(0, N_DATA - 1)
    return DATA[i]


def higher(A, B):
    """return True if A win"""

    if A["follower_count"] > B["follower_count"]:
        return "A"
    return "B"


def is_guess_true(A, B):
    """return True guess Guess right"""

    print(f'A : {A["follower_count"]}')
    print(f'B : {B["follower_count"]}')

    guess = input("Who has more followers? Type 'A' or 'B' : ")

    if guess == higher(A, B):
        return True
    return False


def higher_lower():
    score = 0

    should_continue = True
    while should_continue:
        A = data_generator()
        B = data_generator()

        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        print(("Compare A: {0}, a {1}, from"
               " {2}.").format(A['name'], A['description'], A['country']))
        print(art.vs)
        print(("Against B: {0}, a {1},from"
               " {2}.").format(B['name'], B['description'], B['country']))

        should_continue = is_guess_true(A, B)
        if should_continue:
            score += 1
            replit.clear()
        else:
            replit.clear()
            print(art.logo)
            print(f"Sorry that's wrong. Your final score: {score}.")


def main():

    should_continue = True
    while should_continue:
        higher_lower()
        play_again = input("\nDo you want to play again ? Type 'y' for yes: ")
        if play_again != 'y':
            should_continue = False
        replit.clear()


if __name__ == "__main__":
    main()
