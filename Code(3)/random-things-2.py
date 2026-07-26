import random

items = ["Water", "Bottle", "Toy car"]

# Randomly select an item from the list
r = random.choice(items)

# Create a list to store guesses
listss = []
listss.append(r)

while True:
    print("_" * len(r))
    user_input = input("> ").capitalize()
    
    # Check if the input matches the selected item
    if user_input in items:
        if user_input == r:
            print(f"Correct! The word was '{r}'.")
            break
        else:
            print("Wrong guess, try again.")
    else:
        print("Invalid input. Please enter one of the items from the list.")
