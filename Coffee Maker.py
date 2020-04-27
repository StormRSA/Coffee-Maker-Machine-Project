# Stored items:
stored_water = 400
stored_milk = 540
stored_coffee_beans = 120
stored_cups = 9
stored_money = 550

# Coffee requirements:
espresso = [250, 0, 16, 1, 4]  # Arranged from water to money.
latte = [350, 75, 20, 1, 7]  # Arranged from water to money.
cappuccino = [200, 100, 12, 1, 6]  # Arranged from water to money.


# Coffee Machine start up process:
def coffee_machine_startup():
    global stored_water, stored_milk, stored_coffee_beans, stored_cups, stored_money
    print("The coffee machine has:")
    print(stored_water, "of water")
    print(stored_milk, " of milk")
    print(stored_coffee_beans, "of coffee beans")
    print(stored_cups, "of disposable cups")
    print(stored_money, "of money")
    print()


# User actions:
def purchase_coffee():
    global stored_water, stored_milk, stored_coffee_beans, stored_cups, stored_money
    buy_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to return:")

    if buy_input == "1" and stored_water >= espresso[0] and stored_milk >= espresso[1] \
            and stored_coffee_beans >= espresso[2] and stored_cups >= espresso[3]:
        print("I have enough resources, making you a coffee")
        print("Preparing your coffee now.")
        print("Complete please enjoy.")
        print()

        # Changing coffee machine storage values:
        stored_water -= espresso[0]
        stored_milk -= espresso[1]
        stored_coffee_beans -= espresso[2]
        stored_cups -= espresso[3]
        stored_money += espresso[4]

        # Printing new items in storage:
        print("The coffee machine has:")
        print(str(stored_water) + "ml of water")
        print(str(stored_milk) + "ml of milk")
        print(str(stored_coffee_beans) + "g of coffee beans")
        print(str(stored_cups) + " of disposable cups")
        print("$" + str(stored_money) + " of money")
        print()

    elif stored_water < espresso[0]:
        print("Sorry, not enough water.")

    elif stored_milk < espresso[1]:
        print("Sorry, not enough milk.")

    elif stored_coffee_beans < espresso[2]:
        print("Sorry, not enough coffee beans.")

    elif stored_cups < espresso[3]:
        print("Sorry, not enough cups.")

    elif buy_input == "2" and stored_water >= latte[0] and stored_milk >= latte[1] \
            and stored_coffee_beans >= latte[2] and stored_cups >= latte[3]:
        print("I have enough resources, making you a coffee")
        print("Preparing your coffee now.")
        print("Complete please enjoy.")
        print()

        # Changing coffee machine storage values:
        stored_water -= latte[0]
        stored_milk -= latte[1]
        stored_coffee_beans -= latte[2]
        stored_cups -= latte[3]
        stored_money += latte[4]

        # Printing new items in storage:
        print("The coffee machine has:")
        print(str(stored_water) + "ml of water")
        print(str(stored_milk) + "ml of milk")
        print(str(stored_coffee_beans) + "g of coffee beans")
        print(str(stored_cups) + " of disposable cups")
        print("$" + str(stored_money) + " of money")
        print()

    elif stored_water < latte[0]:
        print("Sorry, not enough water.")

    elif stored_milk < latte[1]:
        print("Sorry, not enough milk.")

    elif stored_coffee_beans < latte[2]:
        print("Sorry, not enough coffee beans.")

    elif stored_cups < latte[3]:
        print("Sorry, not enough cups.")

    elif buy_input == "3" and stored_water >= cappuccino[0] and stored_milk >= cappuccino[1] \
            and stored_coffee_beans >= cappuccino[2] and stored_cups >= cappuccino[3]:
        print("I have enough resources, making you a coffee")
        print("Preparing your coffee now.")
        print("Complete please enjoy.")
        print()

        # Changing coffee machine storage values:
        stored_water -= cappuccino[0]
        stored_milk -= cappuccino[1]
        stored_coffee_beans -= cappuccino[2]
        stored_cups -= cappuccino[3]
        stored_money += cappuccino[4]

        # Printing new items in storage:
        print("The coffee machine has:")
        print(str(stored_water) + "ml of water")
        print(str(stored_milk) + "ml of milk")
        print(str(stored_coffee_beans) + "g of coffee beans")
        print(str(stored_cups) + " of disposable cups")
        print("$" + str(stored_money) + " of money")
        print()

    elif stored_water < cappuccino[0]:
        print("Sorry, not enough water.")

    elif stored_milk < cappuccino[1]:
        print("Sorry, not enough milk.")

    elif stored_coffee_beans < cappuccino[2]:
        print("Sorry, not enough coffee beans.")

    elif stored_cups < cappuccino[3]:
        print("Sorry, not enough cups.")

    elif buy_input == "back":
        pass


def machine_refill():
    global stored_water, stored_milk, stored_coffee_beans, stored_cups, stored_money

    stored_water += int(input("Write how many ml of water do you want to add:"))
    stored_milk += int(input("Write how many ml of milk do you want to add:"))
    stored_coffee_beans += int(input("Write how many grams of coffee beans do you want to add:"))
    stored_cups += int(input("Write how many disposable cups of coffee do you want to add:"))
    print()
    print("The coffee machine has:")
    print(stored_water, "of water")
    print(stored_milk, " of milk")
    print(stored_coffee_beans, "of coffee beans")
    print(stored_cups, "of disposable cups")
    print()


def money_withdrawal():
    global stored_money
    print("I gave you $" + str(stored_money))
    stored_money = 0
    print()


user_input = input("Write action (buy, fill, take, remaining, exit): ")
while user_input != "exit":
    if user_input == "buy":
        print()
        purchase_coffee()
    elif user_input == "fill":
        print()
        machine_refill()
    elif user_input == "take":
        print()
        money_withdrawal()
    elif user_input == "remaining":
        print()
        coffee_machine_startup()
    else:
        break
    user_input = input("Write action (buy, fill, take, remaining, exit): ")
