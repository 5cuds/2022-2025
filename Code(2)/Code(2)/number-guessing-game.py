import random

random_limit = random.randint(5, 10)
print("Welcome to the Python Number Guessing Game!\nHere you have to GUESS a random number!")
print("And you have a random amount of trys\nGood luck!\n=====================")

print("(-----Difficulty-----)\n1)Easy mode [1 - 20] \n2)Medium mode [1 - 50\n3)Hard mode [1 - 100]")
difficulty_level = int(input("> "))
if difficulty_level == 1:
    b_number = 20
    random_number = random.randint(1, 20)
elif difficulty_level == 2:
    random_number = random.randint(1, 50)
    b_number = 50
else:
    random_number = random.randint(1, 100)
    b_number = 100

count = 0
limit = random_limit
print(f"You have {limit} trys")


def main():
    global count, limit

    while count < limit:
        try:
            user_input = int(input("===============\nGuess the number: "))

            if count == limit:
                print(f"Correct number was {random_number}")
            elif user_input > b_number:
                print("Choice out of range!")
                main()

            if user_input == random_number:
                print(f"Correct! {random_number} was the correct answer!")
                break
            else:
                print("Incorrect try again..")
                if user_input > random_number:
                    print("Your Guess is a bit high try a new number!")
                elif user_input < random_number:
                    print("Your Guess is a bit low try a new number!")
                elif user_input > b_number or user_input < b_number:
                    print("Choice out of range!")
                count += 1

        except ValueError:
            print("Enter a valid choice!")


if __name__ == '__main__':
    main()
