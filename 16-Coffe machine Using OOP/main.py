from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


play = True
while play:
    answer = input(f"What would you like? {menu.get_items()} ")
    if answer == "off":
        print("Machine is turning off. Good-Bye")
        play = False
    elif answer == "report":
        coffee_maker.report()
        money_machine.report()
    elif answer in menu.get_items():
        drink = menu.find_drink(answer)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)