while True:
    topping = input("What do you want to add to your pizza?\n(Type \"quit\" to stop the program.) ")
    if topping.lower() == "quit":
        break
    else:
        print(f"\033[32mAdding {topping.lower()} to your pizza!\033[0m")