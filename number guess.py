# guess the number

import random

while True:
    ran: int = random.randrange(0, 100)
    count: int = 0

    while True:

        num: int =(input("Guess the  number between 1 to 99: "))
        if num.isdigit():
            num = int(num)

            count += 1
            if ran > num:
                print(f"The number is greater than {num}")

                continue
            elif ran < num:
                print(f"The number is less than {num}")

                continue
            else:

                print(f"You got the right number in {count} turns")

                break

        else:
            print("Please enter the correct number.")
            continue

    play_again: str = input("Do you want to play again?, Yes/No ")
    list_yes = ["yes", "y",]
    if play_again.lower() not in list_yes:
        break
