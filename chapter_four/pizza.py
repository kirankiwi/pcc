my_pizzas = ["Everything Pizza", "Zucchini Pizza", "Pesto Pizza"]

friend_pizzas = my_pizzas[:]

my_pizzas.append("Margherita Pizza")
friend_pizzas.append("Peperoni Pizza")

print("\nMy favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friends favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#for pizza in pizzas:
#    print(f"I like {pizza}.")

#print("I really like pizza!")