def build_sandwich(bread, *toppings):
    print(f"Making a sandwich with {bread.lower()} bread, and the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

build_sandwich("White", "Jam", "butter")
build_sandwich("multigrain", "hummus", "lettuce", "Tomato", "Pickles")
build_sandwich("gluten-free", "Peanut butter", "Jam")