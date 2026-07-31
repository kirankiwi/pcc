response_num = 0
responses = {}
while response_num <= 3:
    name = input("What is your name?").title()
    place = input("What is your dream vacation location?").title()
    responses[name] = place
    response_num += 1
for name, response in responses.items():
    print(f"{str(name).title()}'s dream vacation location is {str(response).title()}.")
