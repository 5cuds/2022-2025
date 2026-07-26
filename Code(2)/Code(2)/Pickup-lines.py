import random
print("Welcome To The Pickup Line Generator")
print("========================================")

pick_up = [
    "I'd like to take you to the movies but they don't let you bring your own snacks in.",
    "No pen, no paper but you still draw my attention.",
    "All the good pick up lines are taken but you aren't",
    "Excuse me while I delete my dating apps.",
    "This must be a museum because you're a work of art.",
    "Are you WiFi? Because I feel a connection",
    "I'm not even playing cards but somehow I pulled a Queen.",
    "You must be a dog person because you look fetching.",
    "I didn't even have to run to catch these butterflies.",
    "Well, here I am. What are your other two wishes?",
    "Hey, how was heaven when you left it?"
]

def pickup_lines():
    choice_random = random.choice(pick_up)
    print("============================")
    print(choice_random)

def pickup():
    user_input = input("Generate? (Yes/No): ").lower()
    if user_input == "yes":
        print("Great")
        print("===========")
    elif user_input == "no":
        print("-999 rizz")
        quit()
    else:
        print("Invalid choice")
        print("============================")
        pickup()

    while True:
        user_input_int = int(input("How many: "))
        if user_input_int > 10:
            print("(MAX) 10")
        elif user_input_int < 1:
            print("(MIN) 1")
        else:
            for i in range(user_input_int):
                pickup_lines()
            break


pickup()
