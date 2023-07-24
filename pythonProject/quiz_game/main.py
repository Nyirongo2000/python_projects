score =0
print("welcome to my computer quiz! ")

playing = input("Do you like to play? \n yes \n no \n :")
if playing.lower() !="yes":
    quit()

print("lets play ! ");
answer = input("what does CPU stand for? ")
if answer.lower() == "central proccesing unit":
    print('correct!');
    score += 1
else:
    print("incorect")

answer = input("what does CPU stand for? ")
if answer.lower() == "central proccesing unit":
    print('correct!');
    score += 1
else:
    print("incorect")

answer = input("what does CPU stand for? ")
if answer.lower() == "central proccesing unit":
    print('correct!');
    score += 1
else:
    print("incorect")

print("you got "+str(score) +" questions correst")
print("you got "+str((score/4)*100) +"%")