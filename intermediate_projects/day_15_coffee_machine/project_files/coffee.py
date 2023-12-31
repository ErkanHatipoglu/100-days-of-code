"""This module simulates a virtual coffee machine. It provides users with various options like selecting a beverage
from a predefined menu, turning the machine off, or getting a report on the current status of resources. The menu
includes options like espresso, latte, and cappuccino, each with its own ingredients and cost."""

from art import logo  # Importing the 'art' library for the 'logo' graphic.

# Defining the menu for the coffee machine. Each beverage type (espresso, latte, cappuccino) has its specific
# ingredients and cost.
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

# Defining the available resources in the coffee machine (water, milk, coffee) with their quantities.
resources = dict(water=300, milk=200, coffee=100)

total_money = 0  # Tracks the total money accumulated by the coffee machine.

coin_values = dict(quarters=0.25, dimes=0.10, nickels=0.05, pennies=0.01)  # Denominations of coins and their
# respective values.


def get_user_choice(menu):
    """
    Prompt the user to choose an action from the menu, which can be selecting a beverage, turning off the machine,
    or getting a report on resources.

    Args:
    menu (dict): A dictionary containing the beverage options available in the menu.

    Returns:
    str: The user's selected action.
    """
    options = "/".join(menu)
    return input(f"What would you like? ({options}): ").lower()


def display_machine_status(current_resources, money):
    """
    Displays the current status of resources and money in the coffee machine.

    Args:
    current_resources (dict): The current quantities of resources (water, milk, coffee) in the machine.
    money (float): The total amount of money accumulated by the machine.

    Prints the status of each resource and the total money.
    """
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(beverage, available_resources, menu):
    """
    Checks if the machine has enough resources to prepare the requested beverage.

    Args:
        beverage (str): Type of beverage to prepare.
        available_resources (dict): Current quantities of resources in the machine.
        menu (dict): Details of beverages and their required ingredients.

    Returns:
        bool: True if resources are sufficient, False otherwise.
    """
    water_amount = int(available_resources['water'])
    milk_amount = int(available_resources['milk'])
    coffee_amount = int(available_resources['coffee'])
    missing_ingredients_list = []

    if "water" in menu[beverage]['ingredients']:
        if water_amount < menu[beverage]['ingredients']['water']:
            missing_ingredients_list.append('water')

    if "milk" in menu[beverage]['ingredients']:
        if milk_amount < menu[beverage]['ingredients']['milk']:
            missing_ingredients_list.append('milk')

    if "coffee" in menu[beverage]['ingredients']:
        if coffee_amount < menu[beverage]['ingredients']['coffee']:
            missing_ingredients_list.append('coffee')

    if len(missing_ingredients_list) > 0:
        missing_ingredients = " and ".join(missing_ingredients_list)
        print(f"Sorry there is not enough {missing_ingredients}!")
        return False
    else:
        return True


def process_coins(coin_dict):
    """
    Calculates the total amount of money inserted by the user based on the coin denominations.

    Args:
        coin_dict (dict): Dictionary with coin denominations and their values.

    Returns:
        float: Total amount of money inserted.
    """

    total_inserted_money = 0
    print("Please insert coins.")  # Prompting the user to insert coins for payment.
    for key in coin_dict:
        total_inserted_money += coin_dict[key] * float(input(f"how many {key}?: "))
    return total_inserted_money


def check_transaction(inserted_money, beverage_price):
    """
    Checks if the inserted amount of money is sufficient to purchase the selected beverage.

    Args:
        inserted_money (float): The total amount of money inserted by the user.
        beverage_price (float): The cost of the selected beverage.

    Returns:
        bool: True if the transaction is successful (enough money inserted), False otherwise.
    """
    if inserted_money < beverage_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif inserted_money == beverage_price:
        return True
    else:
        print(f"Here is ${round((inserted_money - beverage_price), 2)} dollars in change.")
        return True


def make_coffee(available_resources, selected_beverage, menu):
    """
    Prepares the selected beverage by deducting the required resources.

    Args:
        available_resources (dict): Current quantities of resources in the machine.
        selected_beverage (str): The beverage chosen by the user.
        menu (dict): Details of beverages and their required ingredients.

    Prints a message once the beverage is prepared.
    """
    for key in menu[selected_beverage]["ingredients"]:
        available_resources[key] -= menu[selected_beverage]["ingredients"][key]
    print(f"Here is your {selected_beverage} ☕️. Enjoy!")


user_action = ""  # Stores the user's selected action.
exit_program = False  # Flag to control the main program loop.
print(logo)  # Display the logo of the virtual coffee machine.

while not exit_program:
    # Main loop for operating the coffee machine. It continues until 'exit_program' is set to True.

    user_action = get_user_choice(MENU)  # Get the user's choice of action from the menu.

    if user_action == 'off':
        print("Closing off. Please wait...")
        exit_program = True  # Exit the program if the user selects 'off'.
    elif user_action == 'report':
        display_machine_status(resources, total_money)  # Display the current status.
    elif user_action in MENU.keys():
        sufficient_resources = check_resources(user_action, resources, MENU)

        if sufficient_resources:
            # Implement coin processing functionality.
            total_inserted_amount = process_coins(coin_values)

            # Implement transaction verification.
            has_enough_money = check_transaction(total_inserted_amount, MENU[user_action]["cost"])

            if has_enough_money:
                total_money += MENU[user_action]["cost"]  # Update total money in the machine

                # Implement coffee making process.
                make_coffee(resources, user_action, MENU)
    else:
        print('Wrong Input')  # Inform the user of an incorrect input.
