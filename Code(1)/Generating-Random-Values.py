import random
#for i in range():
#        print(random.random())

#members = ["Mosh", "Nihal", "Bob", "Tom", "John", "Mia", "Kevin", "Jimmy"]
#leader=random.choice(members)
#print(leader)

class Dice:
        def roll(self):
                first=random.randint(1, 6)
                last = random.randint(1, 6)
                return first, last
dice1 = Dice()
print(dice1.roll())