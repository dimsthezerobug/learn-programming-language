############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import replit
import art

CARD_DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

info = {
    "computer": {"hand": [], "score": 0,},
    "human": {"hand": [], "score": 0, },
}

def get_card(player):
    """menambahkan hand angka random, juga menghitung totalnya"""

    card = random.choice(CARD_DECK)
    current_hand = info[player]["hand"]
    current_hand.append(card)
    info[player]["score"] += card

def special_case(player):
    """special case jika ada angka 11 di dalam hand saat total melebihi 21, angka 11 angka diganti 1"""
    # jika ada angka 11 di hand
    # maka 11 akan jadi 1

    player_hand = info[player]["hand"]
    # player_score = info[player]["score"]
    n = len(player_hand)

    for i in range(n):
        if player_hand[i] == 11: 
            player_hand[i] = 1
            info[player]["score"] -= 10  # NOTE saat angka 11 di ganti 1, terjadi pengurangan score -10
            if info[player]["score"] <= 21:
                break

def computer_play():
    """computer akan terus mengambil kartu selama scorenya dibawah 17"""

    # NOTE komputer akan terus mengambil kartu 
    # saat score < 17

    while info["computer"]["score"] < 17:
        get_card("computer")
        
        # print(info["computer"]["hand"])

        if info["computer"]["score"] > 21:
            special_case("computer")

    # print(info["computer"]["score"])

def human_play():
    get_card("human")
    get_card("human")

    # print(info["human"]["hand"])
    # print(info["human"]["score"])

    def score_less_than_21():
        if info["human"]["score"] == 21:
            return False
        elif info["human"]["score"] > 21:
            special_case("human")
            if info["human"]["score"] < 21:
                return True
            return False
        return True
    
    should_continue = score_less_than_21()

    # print(should_continue)

    while should_continue:
        
        print(f"\tYour cards: {info['human']['hand']}", end="")
        print(f", current score: {info['human']['score']}")

        print(f"\tComputer's first card: {info['computer']['hand'][0]}")

        get_another_card = input("Type 'y' to get another card: ")
        
        if get_another_card == "y":
            get_card("human")
            should_continue = score_less_than_21()
            # print(should_continue)
        else:
            should_continue = False

def reset_info():
    info["computer"]["hand"] = []
    info["computer"]["score"] = 0
    info["human"]["hand"] = []
    info["human"]["score"] = 0

    

def blackjack():
    print(art.logo)

    computer_play()
    human_play()

    computer_score = info["computer"]["score"]
    human_score = info["human"]["score"]

    print(f"\tYour final hand: {info['human']['hand']}, final score: {human_score}")
    print(f"\tComputer's final hand: {info['computer']['hand']}, final score: {computer_score}")

    win = "\nYOU WIN\n"
    lose = "\nYOU LOSE\n"
    draw = "\nDRAW\n"

    if human_score > 21:
        print(lose)
    elif human_score == computer_score:
        print(draw)
    elif human_score == 21:
        print(win)
    elif human_score < 22:
        if computer_score > 21:
            print(win)
        elif human_score > computer_score:
            print(win)
        else: 
            print(lose)
    else:
        print(lose)
        
    reset_info()

    restart = input("Do you want to play again? type 'y' for yes: ")

    if restart == "y":
        replit.clear()
        blackjack()
    else:
        print("Game Stopped")

def main():
    start = input("Do you want to play Blackjack Game ? type 'y' for yes: ")

    if start == "y":
        blackjack()
    else:
        print("Game Stopped")


if __name__ == "__main__":
    main()
