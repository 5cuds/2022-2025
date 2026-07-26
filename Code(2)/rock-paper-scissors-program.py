import random
computer = random.randint(1, 3)


def game():
    while True:
        user_input = int(input("==============\n1)Rock[🤘]\n2)Scissors[✂]\n3)Paper[📄]\n==============\n> "))
        print("==============")
        if user_input == 1:
            user_choice = "Rock"
        elif user_input == 2:
            user_choice = "Scissors"
        else:
            user_choice = "Paper"
        if computer == 1:
            com1 = "Rock"
        elif computer == 2:
            com1 = "Scissors"
        else:
            com1 = "Paper"
        if user_input == computer:
            print(f"Player: {user_choice}\nComputer: {com1}\nIs a draw..")
            quit()
        elif user_input == 1:
            if computer == 3:
                print(f"Player: {user_choice}\nComputer: {com1}\nThe Computer Has Won!")
                quit()
            else:
                print(f"Player: {user_choice}\nComputer: {com1}\nThe Player Has Won!")
                quit()
        elif user_input == 2:
            if computer == 1:
                print(f"Player: {user_choice}\nComputer: {com1}\nThe Computer Has Won!")
                quit()
            else:
                print(f"Player: {user_choice}\nComputer: {com1}\nThe Player Has Won!")
                quit()
        elif user_input == 3:
            if computer == 2:
                print(f"Player: {user_choice}\nComputer: {com1}\nThe Computer Has Won!")
                quit()
            else:
                print(f"Player: {user_choice}\nComputer: {com1}\nThe Player Has Won!")
                quit()
        else:
            print("Enter a valid choice")


game()
