master_password = input("what is the master password ?")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            #print(line.rstrip())
            #split the read data on each pipe
            data = line.rstrip()
            user, passw = data.split("|")
            print("user: ", user, "| password: ",passw)
def add():
    name = input('account name: ')
    pwd = input('Password: ')

    # we dont require to open and close the file
    with open('password.txt', 'a') as f:
        f.write(name + " | " +pwd + "\n")

while True:
    mode = input("would you like to add a new password or view existing ones (view,add) or q to quit: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue


