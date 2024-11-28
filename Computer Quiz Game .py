import random

user_wins = 0
computer_wins = 0
options =['Rock,' 'Paper', 'scissors']

while True:
    user_inputs = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_inputs == "q":
        break
    if user_inputs not in options:
        continue
    random_number =random.randint(0,2)
    #

print("Goodbye!")