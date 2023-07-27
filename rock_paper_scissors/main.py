# keeps track of either the user wins or the computer wins

import random

user_wins = 0
computer_wins=0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("type Rock/Paper/scissors or q to quit: ").lower()
    if user_input =="q":
        break
        # quit()
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    #rock: 0 , paper: 1, scissors:2

    computer_pick = options[random_number]
    print("computer picked ", computer_pick+ ".")

    if user_input =="rock" and computer_pick == "scissors":
        print("you won!")
        user_wins +=1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1

    elif user_input == "scisssors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1
    else:
        print("you lost!")
        computer_wins +=1


print("you won",user_wins, "times")
print("you won",computer_wins, "times")
print("exited")
