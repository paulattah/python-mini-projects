import random


top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("please tpy a number larger than 0 next time ")
        quit()

else:
    print("Please type a number next time ")
    quit()

random_number = random.randint(1, 10)
guesses = 0

while True:
    guesses +=1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)


    else:
        print("Please type a number next time ")
        continue
    if user_guess == random_number:
        print("you got it!")
        break

    elif user_guess > random_number:
        print ("you were above the number")
    else:

        print ("you were below the number ")

print ("you got it in", guesses, "guesses")

   
