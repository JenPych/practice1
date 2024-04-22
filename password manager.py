## import os ##


def add():
    user = input("Enter a username: ")
    password = input("Enter a new password: ")

    with open("password.txt", 'a') as file:
        file.write(f"{user} | {password} \n")


def view():
    with open("password.txt", 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            stored_user, stored_pass = data.split('|')
            print(f"Username: {stored_user} Password: {stored_pass}")


master_pass: str = input("Enter the master key: ")

if master_pass == "xxx":
    print("Welcome!")
    while True:
        prompt = input("Press 'a' to add a new password, \n"
                       "Press 'v' to check existing password. \n"
                       "Press 'q' to quit: ")

        if prompt == 'a':
            add()
        elif prompt == 'v':
            view()
        elif prompt == "q":
            print("Password manager closed.")
            quit()
        else:
            print("Error in input. Try again.")
            continue
else:
    print("Wrong key entered.")
    quit()

