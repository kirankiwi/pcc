def country_city(city, country):
    return f"{city}, {country}"


cities = {
    "Christchurch": "New Zealand",
    "Boulder": "USA",
    "Tokyo": "Japan",
}

for city, country in cities.items():
    print(country_city(city, country))