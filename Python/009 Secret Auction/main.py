from replit import clear
import art

print(art.logo)
print("\n\nWelcome to secret auctionn program.")
#HINT: You can call clear() to clear the output in the console.
bid_log = {} #bid_log{bid : name}

def add_new_bid():
    name = input("what is your name? ")
    bid = int(input("What's your bid? $"))

    bid_log[bid] = name

def other_bidder():
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidder == "yes":
        return True
    return False

add_new_bid()
there_is_other_bidder = other_bidder()

while there_is_other_bidder:
    clear()
    add_new_bid()
    there_is_other_bidder = other_bidder()

the_winner_bid = 0

for bid in bid_log:
    if bid > the_winner_bid:
        the_winner_bid = bid
    
the_winner_name = bid_log[the_winner_bid]

print(f"The winner is {the_winner_name} with a bid of ${the_winner_bid}.")
