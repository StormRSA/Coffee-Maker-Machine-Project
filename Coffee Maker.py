user_input = int(input("Write how many cups of coffee you will need: > "))

# Variables for cup of coffee
water = 200
milk = 50
coffee_beans = 15

# Logic:
if user_input:
    # Int to string conversion:
    user_input_conversion = str(user_input)
    required_water = str(water * user_input)
    required_milk = str(milk * user_input)
    required_coffee_beans = str(coffee_beans * user_input)

    print("For " + user_input_conversion + " cups of coffee you will need:")
    print(required_water + "ml of water")
    print(required_milk + "ml of milk")
    print(required_coffee_beans + "g of coffee beans")

print('''
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
''')