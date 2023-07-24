import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than 0 next time")
        quit()

else:
    print("please type a number next time. ")
    quit()

r = random.randint(1, top_of_range)
gues_count = 0
while True:
    gues_count += 1
    user_guess = input("make a gues: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time. ")
        continue
    if user_guess == r:
        print('you got it !')
        break
    elif gues_count > r:
        print("you guessed bellow the number")
    else:
        print("you guessed above the number")

print("you got it in", gues_count, "guesses")