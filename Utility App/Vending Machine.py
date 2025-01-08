# CODE LAB 1
# ASSESSMENT 2 -UTILITY APP
# TO create your vending machine

print("""\033[31m]

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ███╗░░░███╗██╗░░░██╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ████╗░████║╚██╗░██╔╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ██╔████╔██║░╚████╔╝░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██║╚██╔╝██║░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ██║░╚═╝░██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░

██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝\033[0m""")

print("\033[1m\033[36m\n\t\t\t\t what you like to buy?\n\033[0m")

# print the menu list for the user
Sweet_snacks = {
    "C1": {"Name": "honey cake", "price": 8, "stock": 4},
    "C2": {"Name": "chocolate cake", "price": 8.50, "stock": 5},
    "C3": {"Name": "blueberry cake", "price": 8, "stock": 3},
    "D1": {"Name": "white forest cake", "price": 7, "stock": 2},
    "D2": {"Name": "red velvet cake", "price": 7.50, "stock": 3}
}

Soft_drinks = {
    "E1": {"Name": "pepsi", "price": 2.75, "stock": 12},
    "E2": {"Name": "mountain dew", "price": 3.00, "stock": 8},
    "E3": {"Name": "7up", "price": 2.50, "stock": 10},
    "F1": {"Name": "sprite", "price": 2.50, "stock": 11},
    "F2": {"Name": "coco cola", "price": 4.00, "stock": 6}
}

chips_items = {
    "G1": {"Name": "pringles", "price": 4, "stock": 7},
    "G2": {"Name": "cheetos", "price": 3.50, "stock": 7},
    "G3": {"Name": "lays", "price": 4, "stock": 7},
    "H1": {"Name": "doritos", "price": 3, "stock": 7},
    "H2": {"Name": "oman chip", "price": 3.50, "stock": 7}
}

# Function to print the menu of items
def print_menu(items):
    print("Menu:\n")
    for category, category_items in items.items():
        print(category + ":")
        for code, item in category_items.items():
            print(f'{code}: {item["Name"]} ({item["price"]:.2f} dhs)')

# Calling the function with all items
all_items = {
    "Sweet_snacks": Sweet_snacks,
    "Soft_drinks": Soft_drinks,
    "chips_items": chips_items
}

print_menu(all_items)

# Function to get a valid code from the user
def get_code(items):
    while True:
        code = input("Enter the code: ")
        # Check if the code is valid
        for category, category_items in items.items():
            if code in category_items:
                return code
        print("Error: Invalid code. Please try again.")

# Function to get a valid amount of money from the user
def get_money(items, code):
    # To search for item in Sweet_snacks, Soft_drinks and Chips_items dictionaries
    for category, category_items in items.items():
        if code in category_items:
            item = category_items[code]
            break
    else:
        print(f'Error: Invalid code "{code}".')
        return None

    while True:
        try:
            money = float(input(f"The price is {item['price']:.2f} dhs. Please insert money: "))
            # Check if enough money was provided
            if money >= item["price"]:
                return money
            print(f'Error: Not enough money. Please insert {item["price"] - money:.2f} dhs more.')
        except ValueError:
            print("Error: Invalid input. Please enter a valid amount.")

# Function to dispense item and calculate change
def dispense_item(items, code, money):
    # To search for item in Sweet_snacks, Soft_drinks and Chips_items dictionaries
    for category, category_items in items.items():
        if code in category_items:
            item = category_items[code]
            break
    else:
        print(f'Error: Invalid code "{code}".')
        return

    # Check if the item is in stock
    if item["stock"] > 0:
        # Dispense the item and calculate change
        print(f'\nDispensing {item["Name"]}...')
        change = money - item["price"]
        item["stock"] -= 1
        print(f"Returning {change:.2f} dhs change...\n")
    else:
        print(f'\nError: {item["Name"]} is out of stock.')

# Function to suggest additional purchase based on the previous purchase
def suggest_purchase(items, code):
    if code in items["Sweet_snacks"]:
        print("You might also like:")
        for code, item in items["chips_items"].items():
            print(f'{code}: {item["Name"]} ({item["price"]:.2f} dhs)')
    elif code in items["chips_items"]:
        print("You might also like:")
        for code, item in items["Soft_drinks"].items():
            print(f'{code}: {item["Name"]} ({item["price"]:.2f} dhs)')

# Main program
while True:
    # Print the menu of items
    print_menu(all_items)
    # Get a valid code from the user
    code = get_code(all_items)
    # Get a valid amount of money from the user
    money = get_money(all_items, code)
    # Dispense item and calculate change
    if money is not None:
        dispense_item(all_items, code, money)
        # Suggest additional purchase based on previous purchase
        suggest_purchase(all_items, code)
    # Prompt the user to continue or exit
    while True:
        response = input("\nWould you like to make another purchase? (Yes/No): ").strip().lower()
        if response == "yes":
            break
        elif response == "no":

         print("Thank you for using this vending machine. Come again!")
        exit()
    else:
        print("Error: Invalid response. Please try again.")
