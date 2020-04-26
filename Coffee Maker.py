while True:
    # Requirements for coffee:
    coffee_recipe = [200, 50, 15]

    # User inputs
    stored_water = int(input("How many ml of water does the coffee machine have? : "))
    stored_milk = int(input("How many ml of milk does the coffee machine have? : "))
    stored_coffee_beans = int(input("How many grams of coffee beans does the coffee machine have? : "))
    required_coffee = int(input("How many cups of coffee do you need? : "))

    # Calculations:
    cups_of_water = (stored_water // coffee_recipe[0])
    cups_of_milk = (stored_milk // coffee_recipe[1])
    grams_of_beans = (stored_coffee_beans // coffee_recipe[2])

    stored_coffee = min(cups_of_water, cups_of_milk, grams_of_beans)
    excess_coffee = stored_coffee - required_coffee

    if required_coffee == stored_coffee:
        if input("Please type Yes to being preparation: ") == "Yes":
            print("Yes, I can make that amount of coffee.")
            print("_________________________________________________")
            print("Starting to make the coffee... ")
            print("Grinding coffee beans...")
            print("Boiling water...")
            print("Mixing boiled water with crushed coffee beans...")
            print("Pouring coffee into the cup...")
            print("Pouring some milk into the cup...")
            print("Coffee is ready.")
            print("_________________________________________________")
            break

        else:
            print("Turning off")
            break

    elif required_coffee > stored_coffee:
        if stored_coffee == 0:
            print("Please fill up all ingredients please.")
            break

        if stored_coffee >= 1:
            print("No, I can make only", stored_coffee, " cups of coffee.")
            print("Must I still proceed? ")

            if input("Please type Yes to being preparation: ") == "Yes":
                print("Yes, I can make that amount of coffee.")
                print("_________________________________________________")
                print("Starting to make the coffee... ")
                print("Grinding coffee beans...")
                print("Boiling water...")
                print("Mixing boiled water with crushed coffee beans...")
                print("Pouring coffee into the cup...")
                print("Pouring some milk into the cup...")
                print("Coffee is ready.")
                print("_________________________________________________")
                break

            else:
                print("Please restart the process.")
                break
        else:
            print("Please restart the process.")
            break

    else:
        if input("Please type Yes to being preparation: ") == "Yes" or input() == "yes":
            print("Yes, I can make that amount of coffee (and even", excess_coffee, "more than that.)")
            print("_________________________________________________")
            print("Starting to make the coffee... ")
            print("Grinding coffee beans...")
            print("Boiling water...")
            print("Mixing boiled water with crushed coffee beans...")
            print("Pouring coffee into the cup...")
            print("Pouring some milk into the cup...")
            print("Coffee is ready.")
            print("_________________________________________________")
            break

        else:
            print("Please restart the process.")
            break
