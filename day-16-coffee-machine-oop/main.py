from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    # Returns all the names of the available menu items as a concatenated string.
    drink_list = menu.get_items()
    response = input(f"What would you like? ({drink_list}): ").lower()

    if response == "report":
        coffee_maker.report()
        money_machine.report()
    elif response == "off":
        is_on = False
    else:
        drink = menu.find_drink(response)
        # check drink resources available - true or false
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Returns True when payment is accepted, or False if insufficient.
            # make the actual coffee
            coffee_maker.make_coffee(drink)
