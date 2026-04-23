import time

available_toppings = ["Pizza sauce", "Mushroom", "Cheese", "Olives", "Zucchini", "Capsicu"
"m", "Pineapple", "Onion", "Peperoni"]

pizza_toppings = ["Pizza sauce", "Mushroom", "Blueberries", "Cheese", "Olives", "Capsicum"
                  , "Potato", "Onion"]

print("\n")

if not pizza_toppings:
    print("Are you sure you want a plain pizza?")
    print("\n")

for topping in pizza_toppings:
    if topping not in available_toppings:
        print(f"Sorry, we don't have any {topping}.")

if "Pizza sauce" in pizza_toppings:
    time.sleep(0.5)
    print("Adding pizza sauce to your pizza!")
if "Mushroom" in pizza_toppings:
    time.sleep(0.5)
    print("Adding mushrooms to your pizza!")
if "Cheese" in pizza_toppings:
    time.sleep(0.5)
    print("Adding cheese to your pizza!")
if "Zucchini" in pizza_toppings:
    time.sleep(0.5)
    print("Adding zucchini to your pizza!")
if "Olives" in pizza_toppings:
    time.sleep(0.5)
    print("Adding olives to your pizza!")
if "Capsicum" in pizza_toppings:
    time.sleep(0.5)
    print("Adding capsicum to your pizza!")
if "Pineapple" in pizza_toppings:
    time.sleep(0.5)
    print("Adding pineapple to your pizza!")
if "Onion" in pizza_toppings:
    time.sleep(0.5)
    print("Adding onion to your pizza!")
if "Peperoni" in pizza_toppings:
    time.sleep(0.5)
    print("Adding peperoni to your pizza!")

if pizza_toppings:
    time.sleep(1)
    print("\nYour pizza is ready!\n")
    time.sleep(2)