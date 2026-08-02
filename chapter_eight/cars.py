def car(brand, model, **car_info):
    car_info["Manufacturer"] = brand
    car_info["Model"] = model
    return car_info
print(car("Tesla", "Model 3", colour="Blue", seats=5))