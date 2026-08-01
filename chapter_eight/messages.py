# V1

# unsent_messages = ["Hi", "Hello", "Im hungry", "OK", "Bye", "Bye"]

# def print_messages(list):
#     for message in list:
#         print(message)

# print_messages(unsent_messages)

# V2

# unsent_messages = ["Hi", "Hello", "Im hungry", "OK", "Bye", "Bye"]
# sent_messages = []

# def print_messages(list):
#     while list:
#         print(list[0])
#         sent_messages.append(list.pop(0))

# print_messages(unsent_messages)
# print(unsent_messages)
# print(sent_messages)

# V3

unsent_messages = ["Hi", "Hello", "Im hungry", "OK", "Bye", "Bye"]
sent_messages = []

def print_messages(list):
    while list:
        print(list[0])
        sent_messages.append(list.pop(0))

print_messages(unsent_messages[:])
print(unsent_messages)
print(sent_messages)