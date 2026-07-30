cities = {
    "Christchurch": [419200, "New Zealand", 169],
    "Sydney": [5640000, "Australia", 238],
    "Tokyo": [14000000, "Japan", 157]
}

def pop_conversion(pop):
    if pop < 1000:
        return pop
    elif pop < 1000000:
        return f"{pop/1000} thousand"
    else:
        return f"{pop/1000000} million"

for city, stats in cities.items():
    print(f"{city} has a population of {pop_conversion(stats[0])}, is located i"
          f"n {stats[1]} and is {stats[2]} years old."
          )