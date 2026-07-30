person_1 = {
    "first_name": "Nitin",
    "last_name": "Keswani",
    "age": 15,
    "city": "Christchurch"

}

person_2 = {
    "first_name": "Abhinav",
    "last_name": "Keswani",
    "age": 50,
    "city": "Christchurch"
}

person_3 = {
    "first_name": "Kiran",
    "last_name": "Keswani",
    "age": 13,
    "city": "Christchurch"}

people = [person_1, person_2, person_3]

for person in people:
    print(f"\n{person["first_name"]} {person["last_name"]} is {person["age"]} ye"
          f"ars old and lives in {person["city"]}."
          )

# print(f"{person["first_name"]} {person['last_name']} is {person['age']} years"
#       f" old and lives in {person['city']}."
#       )