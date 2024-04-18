# creating a simple quiz game and tallying the total


# asking to start the quiz
answer: str = input("Do you like to play a quiz? ")
total = 0  # adding correct answers into total #
if answer.lower() == "yes":
    print("Lets start the quiz.")
    answer: str = input("What is the largest mammal in the world? ").lower()
    if answer == "whale":
        print("Correct!")
        total += 1
    else:
        print("Wrong answer. Please try again.")
        print(f"You got {total} out of 10 questions correct.")
        quit()

    print(f"{(total / 10) * 100}% complete")
    answer: str = input("What is the largest ocean in the world? ")
    if answer.lower() == "pacific":
        print("Correct!")
        total += 1
    else:
        print("Wrong answer. Please try again.")
        print(f"You got {total} out of 10 questions correct.")
        quit()

    print(f"{(total / 10) * 100}% complete")
    answer: str = input("Which planet is known as the 'Red Planet'? ")
    if answer.lower() == "mars":
        print("Correct!")
        total += 1
    else:
        print("Wrong answer. Please try again.")
        print(f"You got {total} out of 10 questions correct.")
        quit()

    print(f"{(total / 10) * 100}% complete")
    answer: str = input("Who is the CEO of Tesla?'? ")
    if answer.lower() == "elon musk":
        print("Correct!")
        total += 1
    else:
        print("Wrong answer. Please try again.")
        print(f"You got {total} out of 10 questions correct.")
        quit()

    print(f"{(total / 10) * 100}% complete")
    answer: str = input("What is the national fruit of Nepal? ")
    if answer.lower() == "orange" or "oranges":
        print("Correct!")
        total += 1
    else:
        print("Wrong answer. Please try again.")
        print(f"You got {total} out of 10 questions correct.")
        quit()

    print(f"{(total / 10) * 100}% complete")
    answer: str = input("In 'meters', what is the height of Mt. Everest? ")
    if answer.lower() == "8848":
        print("Correct!")
        total += 1
    else:
        print("Wrong answer. Please try again.")
        print(f"You got {total} out of 10 questions correct.")
        quit()

    print(f"{(total / 10) * 100}% complete")
    answer: str = input("What is the full form of 'WHO'? ")
    if answer.lower() == "world health organization":
        print("Correct!")
        total += 1
    else:
        print("Wrong answer. Please try again.")
        print(f"You got {total} out of 10 questions correct.")
        quit()

    print(f"{(total / 10) * 100}% complete")
    answer: str = input("What is the capital of Nepal? ")
    if answer.lower() == "kathmandu":
        print("Correct!")
        total += 1
    else:
        print("Wrong answer. Please try again.")
        print(f"You got {total} out of 10 questions correct.")
        quit()

    print(f"{(total / 10) * 100}% complete")
    answer: str = input("Where is the Eifle tower located? ")
    if answer.lower() == "france" or "paris":
        print("Correct!")
        total += 1
    else:
        print("Wrong answer. Please try again.")
        print(f"You got {total} out of 10 questions correct.")
        quit()

    print(f"{(total / 10) * 100}% complete")
    answer: str = input("Liverpool FC plays in which league? ")
    if answer.lower() == "epl" or "english premier league" or "english league" or "english":
        print("Correct!")
        total += 1
    else:
        print("Wrong answer. Please try again.")
        print(f"You got {total} out of 10 questions correct.")
        quit()

else:
    print("See you again!")

print("!!!Perfect Score!!! \n"
      f"You got {total} out of 10 questions correct.")


# keeping it simple


class Quiz:

    def __init__(self):
        self.total = 0  # adding correct answers into total #

    def question(self, prompt, answers):

        response: str = input(prompt).lower()
        answers: str = [ans.lower() for ans in answers]
        if response in answers:
            print("Correct!")
            self.total += 1
        else:
            print("Wrong answer. Please try again.")
            print(f"You got {self.total} out of 6 questions correct.")
            quit()

    def run(self, collection):
        for prompt, answers in collection:
            self.question(prompt, answers)
            print(f"You got {self.total} correct ")


def main():

    collection = [("What is the largest mammal in the world? ", ["whale"]),
                  ("What is the largest ocean in the world? ", ["pacific"]),
                  ("Which planet is known as the 'Red Planet'? ", ["mars"]),
                  ("Who is the CEO of Tesla?'? ", ["elon musk"]),
                  ("What is the national fruit of Nepal? ", ["orange", "oranges"]),
                  ("Liverpool FC plays in which league? ", ["epl", "english", "english premier league"])]

    start: str = input("Do you like to play a quiz? ")
    if start.lower() == "yes":
        print("Lets start the quiz.")
        quiz = Quiz()
        quiz.run(collection)

    else:
        print("See you again!")


if __name__ == "__main__":
    main()







