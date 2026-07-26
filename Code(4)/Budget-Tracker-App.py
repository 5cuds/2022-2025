import time


my_list = [] # to store the expanses


def add(i, amount): # a func to append my_list
    my_list.append(f"{i} - ${amount:.2f}") 
    print(f"{i.capitalize()} - ${amount:.2f}")


def main():
    """Main Func To Run The Program"""
    try:
        print("(==Welcome To The Python Budget Tracker App!==)\n====================")
        ender_budget = float(input("Enter your Budget: $")) # get the budget from user

        if ender_budget <= 0:
            print("Invalid budget!")
            exit()

        while True:
            print(f"====================\nBudget: ${ender_budget}\n====================\n1)Add\n2)Show\n3)Exit\n====================")
            user_input = int(input("Enter your choice: "))

            if user_input == 1: # Append items to my_list
                item = input("Enter item: ")
                amount = float(input("Enter amount: $"))
                ender_budget -= amount
                add(item, amount)

            elif user_input == 2: # Print my_list
                for i in my_list:
                    print(f"{i}")
                    time.sleep(0.28)
                continue

            elif user_input == 3:  # Exit
                print(f"Thank You For Using Python Budget Tracker App! Final Budget: ${ender_budget}\nGoodBye.")
                exit()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()