import random

u1 = input("Enter a Word: ").capitalize()
u2 = input("Enter a Word: ").capitalize()
u3 = input("Enter a Word: ").capitalize()
u4 = input("Enter a Word: ").capitalize()

lines = [
    f"The {u1} went to the {u2} to buy some {u3} for the {u4}.",
    f"On a {u1} day, I saw a {u2} {u3} in the {u4}.",
    f"On a {u1} day, I saw a {u2} {u3} in the {u3}.",
    f"My favorite way to {u1} is by {u2} with a {u3} while {u4}.",
    f"At the {u1} concert, everyone was {u2} and {u3} with {u4}.",
    f"The {u1} decided to {u2} the {u3} because it was too {u4}.",
    f"During the {u1} storm, I found a {u2} {u3} under the {u4}.",
    f"{u1} and {u2} went to the {u3} to {u4}.",
    f"The {u1} quickly {u2} the {u3} before it {u4}.",
    f"I can't believe the {u1} just {u2} on the {u3} during {u4}!",
    f"In the {u1} of the {u2}, a {u3} was {u4}."
]
random_choice = random.choice(lines)
print("\n"+random_choice)
