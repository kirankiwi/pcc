people = {
    "NKeswani": {
        "first_name": "nitin",
        "last_name": "keswani",
        "age": 15,
        "city": "christchurch"
        },
    "WFang": {
        "first_name": "will",
        "last_name": "fang",
        "age": 13,
        "city": "christchurch"
    },
    "OP": {
        "first_name": "oliver",
        "last_name": "polonowita",
        "age": 13,
        "city": "christchurch"
    }

}

for person, person_info in people.items():
    print(f"Username: {person}\nFull name: {person_info["first_name"].title()} "
          f"{person_info["last_name"].title()}\nLocation: {person_info["city"].title()}\nAge: {person_info["age"]}")

#print(f"{person["first_name"]} {person['last_name']} is {person['age']} years o"
#      f"ld and lives in {person['city']}."
#      )