import random

user_win = 0
comp_win = 0
while True:
    outcomes = ["rock", "paper", "scissors"]
    computer_call = random.choice(outcomes)

    user_call = input("rock, paper, scissors, or quit? ").lower()

    if user_call == "quit":
        print("See you!")
        quit()

    elif user_call in outcomes:

        if user_call == computer_call:
            print("Same pick. Try again!")

        elif (user_call == "rock" and computer_call == "scissors") or \
             (user_call == "paper" and computer_call == "rock") or \
             (user_call == "scissors" and computer_call == "paper"):
            print(f"Computer calls {computer_call}")
            print("You win!")

            user_win += 1

        else:
            print(f"Computer calls {computer_call}")
            print("Computer wins!")
            comp_win += 1

        print(f"User wins: {user_win}")
        print(f"Computer wins: {comp_win}")

    else:
        print("Invalid choice. Please try again.")

