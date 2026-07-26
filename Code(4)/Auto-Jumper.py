import pyautogui
import time
import random


def main():
    print("(=====Welcome to Roblox Auto-Jumper!=====)")

    while True:
        try:

            # Print menu
            print("1)LOS Ring Farming\n2)Roblox AFK Blocker\n3)Hold Down A Key (W, A, S, D)\n4)Custom\n==================")
            user_input = int(input("> "))

            # Print separator
            print("==================")

            if user_input == 1:

                # LOS Ring Farming
                print("LOS Ring Farming mode selected.\n==================")

                while True:
                    # Sleep for 6 seconds
                    time.sleep(6)
                    # Press space
                    pyautogui.press("space")

            elif user_input == 2:

                # Roblox AFK Blocker
                print("Roblox AFK Blocker mode selected.\n==================")

                # Move mouse to random position
                while True:
                    pyautogui.moveTo(random.randint(1, 1000), random.randint(1, 1900), duration=3.5)
                    time.sleep(1) # Move in every 50 seconds

            elif user_input == 3:

                # Hold Down A Key (W, A, S, D)
                print("Hold Down A Key mode selected.\n==================")

                choices = ("W", "A", "S", "D")

                while True:

                    users_choice = input("Enter your choice (W, A, S, D): ").upper().strip()

                    if users_choice in choices:

                        # Hold down the key
                        while True:
                            pyautogui.keyDown(users_choice)
                    else:

                        print("Invalid choice. Please enter W, A, S, or D.\n==================")
                        continue
            else:

                # Custom
                print("Custom mode selected.\n==================")

                key = input("Enter your key: ").lower().strip()

                # Print menu
                print("1)Hold\n2)Time\n==================")
                user_input = int(input("> "))

                if user_input == 1:

                    # Hold down the key
                    while True:
                        pyautogui.keyDown(key)
                elif user_input == 2:

                    # Time
                    time1 = float(input("Enter the time in seconds: "))

                    while True:
                        # Sleep for the time
                        time.sleep(time1)
                        # Press the key
                        pyautogui.press(key)
                else:

                    print("Invalid choice. Please enter 1 or 2.\n==================")
                    continue

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

