import random
import time

scenarios = [
        "You are alone.. in a dark forest with only 4 items, what do you do?",
        "You are in a desert.. with only 4 items, what do you do?",
        "You are weak from running.. you only have 4 items, what do you do?",
        "You are happy!.. you only have 4 items, what do you do?",
        "You are being followed a weird looking man.. you only have 4 items, what do you do?"
]

random_scenarios = random.randint(1, 5)


def lists1():
    print("----------------------")
    print("1)Walk")
    print("2)Sit")
    print("3)Run")
    print("4)Drink water")
    print("5)Use the flashlight")

    user_input = int(input("> "))

    if random_scenarios == 0:
        while True:
            print("You are alone.. in a dark forest with only 4 items, what do you do?")
            lists1()
            user_input1 = int(input("> "))
            if user_input1 == 5:
                print("Correct!\n==============\nCould use some help from the light!")
                break
            else:
                print("Incorrect\n==============\nMaybe could have used the flashlight..")
                break
