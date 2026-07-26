import random

print("(----Python RPS----)")
players_score = 0
computers_score = 0

while True:
    try:
        computer = random.choice(["Rock[🗿]", "Paper[📄]", "Scissors[✂]"])

        user_input = int(input("===============\n1)Rock[🗿]\n2)Paper[📄]\n3)Scissors[✂]\n===============\n> "))
        print("===============")

        if user_input > 3 or user_input < 1:
            print("Enter a valid choice")
            continue

        user_choice = {1: "Rock[🗿]", 2: "Paper[📄]", 3: "Scissors[✂]"}

        if computer == user_choice[user_input]:
            print(f"Player: {user_choice[user_input]}\nComputer: {computer}\nIt's a draw 🤝") 
        elif computer == "Rock[🗿]" and user_input == 3:
            print(f"Player: {user_choice[user_input]}\nComputer: {computer}\nThe Computer Has Won! 🤖")
            computers_score += 1
        elif computer == "Paper[📄]" and user_input == 1:
            print(f"Player: {user_choice[user_input]}\nComputer: {computer}\nThe Computer Has Won! 🤖")
            computers_score += 1
        elif computer == "Scissors[✂]" and user_input == 2:
            print(f"Player: {user_choice[user_input]}\nComputer: {computer}\nThe Computer Has Won! 🤖")
            computers_score += 1
        else:
            print(f"Player: {user_choice[user_input]}\nComputer: {computer}\nThe Player has Won!")
            players_score += 1
        
        play = input("===============\nWhat To Play Again? (Y/N): ").strip().lower()
        if play != "y":
            print(f"===============\nPlayer's Score: {players_score}\nComputer's Score: {computers_score}")
            break

    except ValueError:
        print("Error! Please enter a number.")
