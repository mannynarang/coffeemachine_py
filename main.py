
import menu

user_money = {"quarters": 0,
              "dimes": 0,
              "nickles": 0,
              "pennies": 0
              }


def report():
    print(f"Water: {menu.resources['water']}ml")
    print(f"Milk: {menu.resources['milk']}ml")
    print(f"Coffee: {menu.resources['coffee']}g")
    print(f"Money: ${menu.resources['money']}")


def check_resources(water, milk, coffee):
    if water > menu.resources['water']:
        print(water)
        print(menu.resources['water'])
        print("Sorry there is not enough water")
        return False
    elif milk > menu.resources['milk']:
        print("Sorry there is not enough milk")
        return False
    elif coffee > menu.resources['coffee']:
        print("Sorry there is not enough coffee")
        return False
    return True


def process_coins():
    user_money["quarters"] = int(input("how many quarters? : ")) * .25
    user_money["dimes"] = int(input("how many dimes? : ")) * .10
    user_money["nickles"] = int(input("how many nickles? : ")) * .05
    user_money["pennies"] = int(input("how many pennies? : ")) * .01

    return user_money["quarters"] + user_money["dimes"] + user_money["nickles"] + user_money["pennies"]


def process_transaction(user_payment, coffee_cost):
    if user_payment >= coffee_cost:
        return True
    else:
        False


def make_coffee(water, milk, coffee, money):
    menu.resources['water'] -= water
    menu.resources['milk'] -= milk
    menu.resources['coffee'] -= coffee
    menu.resources['money'] += money


def coffee_machine():
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee_choice == "report":
        report()
        coffee_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee_choice == "off":
        return
    if coffee_choice == "espresso":
        milk = 0
    else:
        milk = menu.MENU[coffee_choice]['ingredients']['milk']

    coffee = menu.MENU[coffee_choice]['ingredients']['coffee']
    water = menu.MENU[coffee_choice]['ingredients']['water']
    money = menu.MENU[coffee_choice]['cost']

    if check_resources(water, milk, coffee):
        amount = process_coins()
        if process_transaction(amount, menu.MENU[coffee_choice]['cost']):
            change = round(amount - menu.MENU[coffee_choice]['cost'], 2)
            print(f"Here is your ${change} in change")
            make_coffee(water, milk, coffee, money)
            print(f"Here is your {coffee_choice}! Enjoy!")
            coffee_machine()
        else:
            print("Not enough money inserted! Money refunded")
            coffee_machine()
    else:
        print("Machine needs service!")
        return


coffee_machine()
