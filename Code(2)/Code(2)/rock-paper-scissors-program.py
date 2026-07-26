import random


def main():
    try:
        computer = random.choice(["Rock[🗿]", "Paper[📄]", "Scissors[✂]"])
        print("(----Python RPS----)")

        user_input = int(input("===============\n1)Rock[🗿]\n2)Paper[📄]\n3)Scissors[✂]\n===============\n> "))
        print("===============")

        if user_input == 1:
            user_choice = "Rock[🗿]"
        elif user_input == 2:
            user_choice = "Paper[📄]"
        else:
            user_choice = "Scissors[✂]"

        if user_choice == computer:
            print(f"Player: {user_choice}\nComputer: {computer}\nIs a draw 🤝")
            
        elif user_choice == "Rock[🗿]":
            if computer == "Paper[📄]":
                print(f"Player: {user_choice}\nComputer: {computer}\nThe Computer Has Won! 🤖")
            else:
                print(f"Player: {user_choice}\nComputer: {computer}\nThe Player Has Won! 🏆")

        elif user_choice == "Paper[📄]":
            if computer == "Scissors[✂]":
                print(f"Player: {user_choice}\nComputer: {computer}\nThe Computer Has Won! 🤖")
            else:
                print(f"Player: {user_choice}\nComputer: {computer}\nThe Player Has Won! 🏆")

        elif user_choice == "Scissors[✂]":
            if computer == "Rock[🗿]":
                print(f"Player: {user_choice}\nComputer: {computer}\nThe Computer Has Won! 🤖")
            else:
                print(f"Player: {user_choice}\nComputer: {computer}\nThe Player Has Won! 🏆")
        else:
            print("Enter a valid choice")

        play = input("===============\nPlay again? (Yes/No): ").upper().strip()
        if play != "YES":
            exit()
        else:
            main()

    except ValueError:
        print("Error!")


if __name__ == '__main__':
    main()
