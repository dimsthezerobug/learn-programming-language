from art import logo
# import replit

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


def show_report():
    # print("\n fungsi show_report")

    print(f"\tWater  : {resources['water']}ml")
    print(f"\tMilk   : {resources['milk']}ml")
    print(f"\tCoffee : {resources['coffee']}g")
    print(f"\tMoney  : ${resources['money']}")


def check_resources(drink):
    enough = True
    ingredients_are_lacking = ""
    required = MENU[drink]['ingredients']

    i = 0
    for ingredients in required:
        if resources[ingredients] < required[ingredients]:
            if i > 0:
                ingredients_are_lacking += f", {ingredients}"
            else:
                ingredients_are_lacking += f"{ingredients}"
            enough = False
            i += 1
    if not enough:
        print(f"\n\tSorry there is not enough {ingredients_are_lacking}.")

    return enough


def process_coin(drink):
    quarters = float(input("\thow many quarters? : "))
    dimes = float(input("\thow many dimes?    : "))
    nickles = float(input("\thow many nickles?  : "))
    pennies = float(input("\thow many pennies?  : "))
    coins = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    cost = MENU[drink]['cost']
    if coins < cost:
        print("\n\tSorry that's not enough money. Money refunded.")
        return False
    else:
        resources['money'] += cost
        print("\n\tHere is ${:0.2f} dollars in change.".format(coins-cost))
        return True


def reduce_resources(drink):
    for ingredients in MENU[drink]['ingredients']:
        resources[ingredients] -= MENU[drink]['ingredients'][ingredients]


def make(drink):
    enough_resources = check_resources(drink)

    if enough_resources:
        enough_coins = process_coin(drink)
        if enough_coins:
            print(f"\tHere is your {drink}. Enjoy!")
            reduce_resources(drink)


def command():
    command = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    print("")
    if command == 'report':
        show_report()
    elif command == "espresso" or "latte" or "cappuccino":
        order = command.upper()
        print(f"\t{order}\n")
        make(command)
    elif command == "off":
        print("Machine is turned off.")


def test():
    print(logo)
    while True:
        command()


if __name__ == "__main__":
    test()
