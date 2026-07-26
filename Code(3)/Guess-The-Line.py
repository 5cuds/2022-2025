import random

lines = {"I Feel soo _ _ _ _": "Good", "Im _ _ _ _ _": "Happy", "I Kinda feel ____": "Sick",
        "Hey Im _ _ _ _": "Here", "Guess The _ _ _ _": "Line", "Im In The _ _ _ _ _ _ _ _": "Bathroom",
        "This is so _ _ _ _ _ _ _ _":"Exciting", "I am feeling very _ _ _ _ _ ": "Tired", "Let's go to the _ _ _ _ ": "Park",
        "Can you see the _ _ _ _ _": "Stars", "It's time to _ _ _ _ _": "Dance", "I need to find my _ _ _ _": "Keys",
        "Today is a _ _ _  day": "Beautiful", "I can't wait to _ _ _ _ _ ": "Relax", "Look at the _ _ _ _ _ _": "Sunset",
        "We should _ _ _ _ Together": "Work", "I just bought a new _ _ _ _": "Book", "The movie was _ _ _ _ _ _ _": "Amazing",
        "I have to finish my _ _ _ _ _ _ _ _": "Homework", "Let's meet at the _ _ _ _": "Cafe", "I'm  so _ _ _ _ _": "Board",
        "I hate _ _ _ _ _ _ _": "Pickles"}

def main():

    random_line = random.choice(list(lines.keys()))

    while True:
        try:

            print(random_line)

            user_input = input("Enter here: ").capitalize().strip()

            if user_input == lines[random_line]:
                print("Correct!")
                main()
            else:
                print("Incorrect try again..")

        except ValueError:
            print("Error")

if __name__ == "__main__":
    main()
