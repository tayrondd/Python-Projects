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
# TODO: 1. Initial Inventory
inventory = {"water": 300,
             "milk": 200,
             "coffee": 100,
             "money": 0}


# TODO: 5. Check resources sufficient?
def inventory_check(drink):
    ingredients = MENU[drink]['ingredients']
    for element in ingredients:
        if ingredients[element] <= inventory[element]:
            inventory[element] = inventory[element] - ingredients[element]
        # if there is not enough of a single element then tell to the operator
        else:
            print(f'Sorry there is not enough {element}')
            return False

play_again = True
while play_again:
    # TODO: 2. Prompt user by asking
    #show menu
    for drinks in MENU:
        print(f"{drinks}--${MENU[drinks]['cost']}")
    answer = input("What would you like? (espresso/latte/cappuccino):")
    #answer = "espresso"

    # TODO: 3. when ask for report and turn off machine
    if answer == "off":
        print("Machine is turning off, Bye!")
        break
    elif answer == "report":
        for key in inventory:
            if key == "coffee":
                print(f"{key}: {inventory[key]}g")
            elif key == "money":
                print(f"{key}: ${inventory[key]}")
            else:
                print(f"{key}: {inventory[key]}ml")

    # TODO: 4. asking for the drink
    elif answer == "espresso" or answer == "latte" or answer == "cappuccino":
        if inventory_check(drink=answer) == False:
            break
        else:
            # TODO: 6. Process coins.
            print("Please insert coins.")
            quarters = int(input("How many quarters?"))
            dime = int(input("How many dime?"))
            nickles = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))

            # calculate the monetary value of coins
            inserted_coins = (quarters * 0.25) + (dime * 0.1) + (nickles * 0.05) + (pennies * 0.01)
            # Check that the user has inserted enough money to purchase the drink they selected.
            if inserted_coins >= MENU[answer]['cost']:
                change = round(inserted_coins - MENU[answer]['cost'], 2)
                inventory['money'] += MENU[answer]['cost']
                print(f"Here is ${change} dollars in change.")
                print(f'Here is your {answer}. Enjoy!”')
                #test
                print(inventory)
            else:
                print(f"“Sorry that's not enough money. ${inserted_coins} Money refunded.")
    else:
        print("wrong choice select another option")