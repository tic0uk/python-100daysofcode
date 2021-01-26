MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
}

balance = {
    "money": 0
}


def print_report(resources_list, available_balance):
    """Return all available resources from resources dictionary"""
    water_left = resources_list["water"]
    milk_left = resources_list["milk"]
    coffee_left = resources_list["coffee"]
    total_money = available_balance["money"]
    return f"Water: {water_left}ml \nMilk: {milk_left}ml \nCoffee: {coffee_left}g \nMoney: ${total_money:0.2f}"


def process_coins():
    """Take user input of coins and returns the sum of them"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickels = int(input("how many nickels?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


def check_resources(drink):
    """Check there is sufficient resources and return true or false"""
    ingredients_to_deduct = (MENU[drink]["ingredients"])
    for key in ingredients_to_deduct:
        if resources[key] < ingredients_to_deduct[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def check_transaction(coins_inserted, cost_drink, machine_balance):
    """check that enough money has been inserted, give change and return the cost balance"""
    if coins_inserted < cost_drink:
        return False
    else:
        if coins_inserted > cost_drink:
            change_given = coins_inserted - cost_drink
            print(f"Here is ${change_given:0.2f} in change.")
        return machine_balance + cost_drink


def make_coffee(drink):
    """deduct the ingredients from overall resources"""
    ingredients_to_deduct = (MENU[drink]["ingredients"])
    for key in ingredients_to_deduct:
        resources[key] -= ingredients_to_deduct[key]


get_me_coffee = True
while get_me_coffee:
    order = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        get_me_coffee = False
    # Print Report on resources
    elif order == "report":
        print(print_report(resources, balance))
    elif order == "latte" or order == "cappuccino" or order == "espresso":
        enough_resources = check_resources(order)
        if enough_resources:
            total_inserted = process_coins()
            cost_of_drink = (MENU[order]["cost"])
            machine_money = balance["money"]
            enough_money = check_transaction(total_inserted, cost_of_drink, machine_money)
            if not enough_money:
                print("Sorry that's not enough money. Money refunded.")
            else:
                balance["money"] = enough_money
                make_coffee(order)
                print(f"Here is your {order}. Enjoy!")
