# Some people I might invite to dinner. These people can be dead or alive.
guests = ['Fletcher','Hafez','Albert Einstien']
print(f"""Dear {guests[0]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"""\nDear {guests[1]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"""\nDear {guests[2]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"\n{guests[1]} can not come.")
guests[1] = 'Max'
print(f"""\nDear {guests[0]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"""\nDear {guests[1]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"""\nDear {guests[2]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print("\nI have a larger table so more people can come.")
guests.insert(0,'Pip')
guests.insert(3,'Emma')
guests.insert(5,'Nina')
print(f"""\nDear {guests[0]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"""\nDear {guests[1]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"""\nDear {guests[2]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"""\nDear {guests[3]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"""\nDear {guests[4]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"""\nDear {guests[5]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print("The larger table will not arrive on time so I can only invite two people.")
print(guests)
guest_who_can_not_be_invited_one = guests.pop(0)
guest_who_can_not_be_invited_two = guests.pop(2)
guest_who_can_not_be_invited_three = guests.pop(3)
guest_who_can_not_be_invited_four = guests.pop(2)
print(f"\nDear {guest_who_can_not_be_invited_one},\nThe table will not arrive on time so you can not come.\n\t- Kiran")
print(f"\nDear {guest_who_can_not_be_invited_two},\nThe table will not arrive on time so you can not come.\n\t- Kiran")
print(f"\nDear {guest_who_can_not_be_invited_three},\nThe table will not arrive on time so you can not come.\n\t- Kiran")
print(f"\nDear {guest_who_can_not_be_invited_four},\nThe table will not arrive on time so you can not come.\n\t- Kiran")
print(f"""\nDear {guests[0]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
print(f"""\nDear {guests[1]},\nCan you come to dinner at 6:00 on Tuesday?\n\t- Kiran""")
del guests[0]
del guests[0]
print(guests)