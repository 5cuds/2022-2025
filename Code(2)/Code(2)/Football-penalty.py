import random
import time

print('''_---------------------_
|                     |
|        O <(Im Tom)  |
|       /|\\           |
|       / \\           |''')
print("Welcome to the Python Football penalty program! ⚽🥅")
print("Enter your choice!")

scored = 0
saved = 0


def football():

    global scored
    global saved

    try:
        print("========================\n1)Top left\n2)Left\n3)Top Right\n4)Right\n========================")
        user_input = int(input("> "))

        if user_input > 4:
            print("========================")
            print("Invalid choice")
            football()

        random_choice = random.randint(1, 4)

        print("========================\nProcessing your choice...")
        print("========================")
        time.sleep(2)

        if random_choice == 1:
            print("Goalkeeper has gone Top left!")
            print('''_---------------------_
|     O               |
|    \\|/              |
|    / \\              |
|                     |''')
        elif random_choice == 2:
            print("Goalkeeper has gone Left!")
            print('''_---------------------_
|                     |
|     O               |
|  ---|---            |
|    / \\              |''')
        elif random_choice == 3:
            print("Goalkeeper has gone Top Right!")
            print('''_---------------------_
|               O     |
|              \\|/    |
|              / \\    |
|                     |''')
        elif random_choice == 4:
            print("Goalkeeper has gone Right!")
            print('''_---------------------_
|                     |
|               O     |
|            ---|---  |
|              / \\    |''')

        if user_input == random_choice:
            print("========================")
            print("The GoalKeeper saved it! 🧤")
            print("Better luck next time!")
            saved += 1
        else:
            print("========================")
            print("YOU SCORED! ⚽")
            print("========================")
            scored += 1

        user_wanna = input("Want to play again? (Y/N): ").lower().strip()
        if user_wanna == "y":
            football()
        else:
            print("========================")
            print(f"Scored: {scored}\nSaved: {saved}")
            exit()

    except ValueError:
        print("Error!")
        football()


football()
