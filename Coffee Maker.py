class CoffeeMachine:

    def __init__(self):
        # Stored items:
        self.stored_water = 400
        self.stored_milk = 540
        self.stored_coffee_beans = 120
        self.stored_cups = 9
        self.stored_money = 550
        self.state = "Online"

        # Coffee requirements:
        self.espresso = [250, 0, 16, 1, 4]  # Arranged from water to money.
        self.latte = [350, 75, 20, 1, 7]  # Arranged from water to money.
        self.cappuccino = [200, 100, 12, 1, 6]  # Arranged from water to money.

    # Coffee machine control states:
    def coffee_machine_control(self):
        while self.state == "Online":
            user_input = input("Write action (buy, fill, take, remaining, exit): ")
            if user_input == "buy":
                print()
                self.purchase_coffee()
            elif user_input == "fill":
                print()
                self.machine_refill()
            elif user_input == "take":
                print()
                self.money_withdrawal()
            elif user_input == "remaining":
                print()
                self.coffee_machine_startup()
            elif user_input == "exit":
                self.state != "Online"
                break

    # Coffee Machine start up process:
    def coffee_machine_startup(self):
        print("The coffee machine has:")
        print(self.stored_water, "of water")
        print(self.stored_milk, " of milk")
        print(self.stored_coffee_beans, "of coffee beans")
        print(self.stored_cups, "of disposable cups")
        print(self.stored_money, "of money")
        print()

    # User actions:
    def purchase_coffee(self):
        buy_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to return:")

        if buy_input == "1" and self.stored_water >= self.espresso[0] and self.stored_milk >= self.espresso[1] \
                and self.stored_coffee_beans >= self.espresso[2] and self.stored_cups >= self.espresso[3]:
            print("I have enough resources, making you a coffee")
            print("Preparing your coffee now.")
            print("Complete please enjoy.")
            print()

            # Changing coffee machine storage values:
            self.stored_water -= self.espresso[0]
            self.stored_milk -= self.espresso[1]
            self.stored_coffee_beans -= self.espresso[2]
            self.stored_cups -= self.espresso[3]
            self.stored_money += self.espresso[4]

            # Printing new items in storage:
            print("The coffee machine has:")
            print(str(self.stored_water) + "ml of water")
            print(str(self.stored_milk) + "ml of milk")
            print(str(self.stored_coffee_beans) + "g of coffee beans")
            print(str(self.stored_cups) + " of disposable cups")
            print("$" + str(self.stored_money) + " of money")
            print()

        # Check for enough ingredients:
        elif self.stored_water < self.espresso[0]:
            print("Sorry, not enough water.")

        elif self.stored_milk < self.espresso[1]:
            print("Sorry, not enough milk.")

        elif self.stored_coffee_beans < self.espresso[2]:
            print("Sorry, not enough coffee beans.")

        elif self.stored_cups < self.espresso[3]:
            print("Sorry, not enough cups.")

        elif buy_input == "2" and self.stored_water >= self.latte[0] and self.stored_milk >= self.latte[1] \
                and self.stored_coffee_beans >= self.latte[2] and self.stored_cups >= self.latte[3]:
            print("I have enough resources, making you a coffee")
            print("Preparing your coffee now.")
            print("Complete please enjoy.")
            print()

            # Changing coffee machine storage values:
            self.stored_water -= self.latte[0]
            self.stored_milk -= self.latte[1]
            self.stored_coffee_beans -= self.latte[2]
            self.stored_cups -= self.latte[3]
            self.stored_money += self.latte[4]

            # Printing new items in storage:
            print("The coffee machine has:")
            print(str(self.stored_water) + "ml of water")
            print(str(self.stored_milk) + "ml of milk")
            print(str(self.stored_coffee_beans) + "g of coffee beans")
            print(str(self.stored_cups) + " of disposable cups")
            print("$" + str(self.stored_money) + " of money")
            print()

        # Check for enough ingredients:
        elif self.stored_water < self.latte[0]:
            print("Sorry, not enough water.")

        elif self.stored_milk < self.latte[1]:
            print("Sorry, not enough milk.")

        elif self.stored_coffee_beans < self.latte[2]:
            print("Sorry, not enough coffee beans.")

        elif self.stored_cups < self.latte[3]:
            print("Sorry, not enough cups.")

        elif buy_input == "3" and self.stored_water >= self.cappuccino[0] and self.stored_milk >= self.cappuccino[1] \
                and self.stored_coffee_beans >= self.cappuccino[2] and self.stored_cups >= self.cappuccino[3]:
            print("I have enough resources, making you a coffee")
            print("Preparing your coffee now.")
            print("Complete please enjoy.")
            print()

            # Changing coffee machine storage values:
            self.stored_water -= self.cappuccino[0]
            self.stored_milk -= self.cappuccino[1]
            self.stored_coffee_beans -= self.cappuccino[2]
            self.stored_cups -= self.cappuccino[3]
            self.stored_money += self.cappuccino[4]

            # Printing new items in storage:
            print("The coffee machine has:")
            print(str(self.stored_water) + "ml of water")
            print(str(self.stored_milk) + "ml of milk")
            print(str(self.stored_coffee_beans) + "g of coffee beans")
            print(str(self.stored_cups) + " of disposable cups")
            print("$" + str(self.stored_money) + " of money")
            print()

        # Check for enough ingredients:
        elif self.stored_water < self.cappuccino[0]:
            print("Sorry, not enough water.")

        elif self.stored_milk < self.cappuccino[1]:
            print("Sorry, not enough milk.")

        elif self.stored_coffee_beans < self.cappuccino[2]:
            print("Sorry, not enough coffee beans.")

        elif self.stored_cups < self.cappuccino[3]:
            print("Sorry, not enough cups.")

        elif buy_input == "back":
            pass

    # Refill ingredients:
    def machine_refill(self):
        self.stored_water += int(input("Write how many ml of water do you want to add: "))
        self.stored_milk += int(input("Write how many ml of milk do you want to add: "))
        self.stored_coffee_beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.stored_cups += int(input("Write how many disposable cups of coffee do you want to add: "))
        print()
        print("The coffee machine has:")
        print(self.stored_water, "of water")
        print(self.stored_milk, " of milk")
        print(self.stored_coffee_beans, "of coffee beans")
        print(self.stored_cups, "of disposable cups")
        print()

    # Collect money from coffee machine:
    def money_withdrawal(self):
        print("I gave you $" + str(self.stored_money))
        self.stored_money = 0
        print()


online = CoffeeMachine()
online.coffee_machine_control()
