import random
import time
print("💊Welcome to RED OR BLUE PILL PROGRAM!💊")
time.sleep(1)
print("You are about to make a choice...")
time.sleep(1)
print("Choose wisely.")


def game():
    try:
        print("---------------------------\n1)Red🔴\n2)Blue🔵")
        user_input = int(input("Choose Red or Blue pill 💊: "))
        if user_input == 2:
            print("You took the blue pill...")
        elif user_input == 1:
            print("You took the red pill...")
        else:
            print("Invalid choice! Choice Red or Blue")
            game()
        print("---------------------------\nProcessing your choice...\n---------------------------")
        time.sleep(1)

        outcome = random.choice([1, 2])

        if user_input == outcome:
            print("Congratulations! You chose the safe pill.😃")
        else:
            print("Oh no! You chose the deadly pill...💀")
            print("Game over.")
        print("---------------------------")
        print("Want to play again?")
        user_input2 = input("(Yes/No): ").lower().strip()
        if user_input2 == "yes":
            game()
        else:
            quit()
    except ValueError:
        print("Invalid choice")
        game()


game()
