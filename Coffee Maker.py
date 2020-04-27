# Stored items:
stored_water = 1200
stored_milk = 540
stored_coffee_beans = 120
stored_cups = 9
stored_money = 550

# Coffee requirements:
espresso = [250, 0, 16, 1, 4]  # Arranged from water to money.
latte = [350, 75, 20, 1, 7]  # Arranged from water to money.
cappuccino = [200, 100, 12, 1, 6]  # Arranged from water to money.

# Start up process:
print("The coffee machine has:")
print(stored_water, "of water")
print(stored_milk, " of milk")
print(stored_coffee_beans, "of coffee beans")
print(stored_cups, "of disposable cups")
print(stored_money, "of money")
print()

# User actions
user_input = str(input("Write action (buy, fill, take):"))
if user_input == "buy":
    buy_input = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))

    if buy_input == 1:
        print("The coffee machine has:")
        print(stored_water - espresso[0], "of water")
        print(stored_milk - espresso[1], " of milk")
        print(stored_coffee_beans - espresso[2], "of coffee beans")
        print(stored_cups - espresso[3], "of disposable cups")
        print(stored_money + espresso[4], "of money")

    elif buy_input == 2:
        print("The coffee machine has:")
        print(stored_water - latte[0], "of water")
        print(stored_milk - latte[1], " of milk")
        print(stored_coffee_beans - latte[2], "of coffee beans")
        print(stored_cups - latte[3], "of disposable cups")
        print(stored_money + latte[4], "of money")

    elif buy_input == 3:
        print("The coffee machine has:")
        print(stored_water - cappuccino[0], "of water")
        print(stored_milk - cappuccino[1], " of milk")
        print(stored_coffee_beans - cappuccino[2], "of coffee beans")
        print(stored_cups - cappuccino[3], "of disposable cups")
        print(stored_money + cappuccino[4], "of money")


elif user_input == "fill":
    water_fill = int(input("Write how many ml of water do you want to add:"))
    milk_fill = int(input("Write how many ml of milk do you want to add:"))
    coffee_beans_fill = int(input("Write how many grams of coffee beans do you want to add:"))
    cups_fill = int(input("Write how many disposable cups of coffee do you want to add:"))
    print()
    print("The coffee machine has:")
    print(stored_water + water_fill, "of water")
    print(stored_milk + milk_fill, " of milk")
    print(stored_coffee_beans + coffee_beans_fill, "of coffee beans")
    print(stored_cups + cups_fill, "of disposable cups")
    print(stored_money, "of money")
    print()

elif user_input == "take":
    str_stored_money = str(stored_money)
    print("I gave you $" + str_stored_money)
    print()
    print("The coffee machine has:")
    print(stored_water, "of water")
    print(stored_milk, " of milk")
    print(stored_coffee_beans, "of coffee beans")
    print(stored_cups, "of disposable cups")
    print(stored_money - stored_money, "of money")
