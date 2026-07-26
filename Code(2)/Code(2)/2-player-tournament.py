import random
import time
print("Welcome to the Python 2 player RPS tournament!\nBest of 3!")
players = [
    "Bob Smith - 👨",
    "Kiddo - 🧑",
    "CumBot - 🤖",
    "Cristino Ronaldo - 🏃‍♂️👦",
    "Lin Dosta - 👩",
    "Paul - 🧑",
    "Waterman - 👨🏼‍🚒"
]
random_player1 = random.choice(players)
random_player2 = random.choice(players)
player1_points = 0
player2_points = 0


def game():

    global player1_points, player2_points

    players1_choice1 = random.choice(["Rock[🗿]", "Paper[📄]", "Scissors[✂]"])
    players2_choice1 = random.choice(["Rock[🗿]", "Paper[📄]", "Scissors[✂]"])

    if players1_choice1 == players2_choice1:
        print("They are choosing...")
        time.sleep(3)
        print(f"{random_player1}: {players1_choice1}\n{random_player2}: {players2_choice1}\nIs a draw 🤝")
        print("=================")
    elif players1_choice1 == "Rock[🗿]":
        if players2_choice1 == "Paper[📄]":
            print("They are choosing...")
            time.sleep(3)
            print(f"{random_player1}: {players1_choice1}\n{random_player2}: {players2_choice1}")
            print(f"=================\n{random_player2} Has Won!\n=================")
            player2_points += 1
        else:
            print("They are choosing...")
            time.sleep(3)
            print(f"{random_player1}: {players1_choice1}\n{random_player2}: {players2_choice1}")
            print(f"=================\n{random_player1} Has Won!\n=================")
            player1_points += 1
    elif players1_choice1 == "Paper[📄]":
        if players2_choice1 == "Scissors[✂]":
            print("They are choosing...")
            time.sleep(3)
            print(f"{random_player1}: {players1_choice1}\n{random_player2}: {players2_choice1}")
            print(f"=================\n{random_player2} Has Won!\n=================")
            player2_points += 1
        else:
            print("They are choosing...")
            time.sleep(3)
            print(f"{random_player1}: {players1_choice1}\n{random_player2}: {players2_choice1}")
            print(f"=================\n{random_player1} Has Won!\n=================")
            player1_points += 1
    elif players1_choice1 == "Scissors[✂]":
        if players2_choice1 == "Rock[🗿]":
            print("They are choosing...")
            time.sleep(3)
            print(f"{random_player1}: {players1_choice1}\n{random_player2}: {players2_choice1}")
            print(f"=================\n{random_player2} Has Won!\n=================")
            player2_points += 1
        else:
            print("They are choosing...")
            time.sleep(3)
            print(f"{random_player1}: {players1_choice1}\n{random_player2}: {players2_choice1}")
            print(f"=================\n{random_player1} Has Won!\n=================")
            player1_points += 1
    else:
        print("Enter a valid choice")


def cheak():
    if player2_points > player1_points:
        print(f"{random_player2} has won the tournament!! 👑🏆")
    elif player1_points > player2_points:
        print(f"{random_player1} has won the tournament!! 👑🏆")
    elif player1_points == player2_points:
        print("It seems like it looks like a draw!")


print(f"Here are the players!:\n{random_player1} (VS) {random_player2}\n=================")
user_input1 = input("Start? (Y/N): ").lower().strip()
if user_input1 == "y":
    print(f"{random_player2} (VS) {random_player1}\n=================")
    game()
    user_input2 = input("Start Round 2? (Y/N): ").lower().strip()
    if user_input2 == "y":
        print("=================")
        game()
        if player2_points == 2:
            print(f"{random_player2} has won the tournament!! 👑🏆")
            exit()
        elif player1_points == 2:
            print(f"{random_player1} has won the tournament!! 👑🏆")
            exit()
        user_input3 = input("Start Round 3? (Y/N): ").lower().strip()
        if user_input3 == "y":
            print('=================')
            game()
        else:
            exit()
    else:
        quit()
else:
    quit()


cheak()
