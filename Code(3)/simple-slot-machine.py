import random
import time

print("(=======Python Slot Machine=======)")

def main(goal):

    items = ["🍉", "🍋", "🍓", "⭐", "🔔"]
    balance = 1000

    while True:
        try:

            if balance == 0:
                print("Game over you lost all of your money lol")
                exit()
            if balance == goal:
                print("Great! You Got To Your Goal.")
                exit()

            print(f"Total balance: ${balance}\nGoal: {goal}\n========================")

            user_amount = int(input("Amount: $"))
                        
            if user_amount <= 0:
                print("Enter a valid a amount.")

            elif user_amount > balance:
                print("insufficient funds")

            else:
                print("========================")
                balance -= user_amount

                view_items = []

                for _ in range(3):
                    randow_item = random.choice(items)
                    view_items.append(randow_item)

                print("Spinning..\n========================")
                time.sleep(3)

                full_items = " | ".join(view_items)
                print(f"      {full_items}")
                print("========================")

                match view_items:

                    case ["🍉", "🍉", "🍉",]:
                        total = user_amount * 2
                        balance += total
                        print(f"You got WATERMELON! 🍉\n+${total}")

                    case ["🍋", "🍋", "🍋",]:            
                        total = user_amount * 3
                        balance += total
                        print(f"You got LEMON! 🍋\n+${total}")

                    case ["🍓", "🍓", "🍓",]:                                                    
                        total = user_amount * 4
                        balance += total
                        print(f"You got STRAWBERRY! 🍓\n+${total}")

                    case ["⭐", "⭐", "⭐"]:                                       
                        total = user_amount * 6
                        balance += total
                        print(f"You got STARS! ⭐\n+${total}")

                    case ["🔔", "🔔", "🔔"]:                                                                     
                        total = user_amount * 7
                        balance += total
                        print(f"You got BELLS! 🔔\n+${total}")
                                
                    case _:
                        print("You won nothing...")

                continue

        except ValueError:
            print("Error!")

if __name__ == "__main__":
    goal1 = int(input("Enter Your Goal: "))
    main(goal1)
