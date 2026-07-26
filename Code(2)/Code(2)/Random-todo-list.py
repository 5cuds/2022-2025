import random
import time

to_do = [
    "Turn on the light",
    "Watch tv",
    "Buy Minecraft",
    "Clean the whole living room",

    "Clean the toilet",
    "Wash the minor",
    "Buy Some toothbrush's",
    "Clean the whole Bathroom",

    "Let the meat cool down",
    "Bake some cookies",
    "Help mom with making rice",
    "Make some hamburger's"
]

random_choice = random.choice(to_do)


class Home:
    clean_living_room = None
    buy_minecraft = None
    buy_toothbrush = None
    clean_bathroom = None
    make_hamburger = None
    turn_on = None
    watch_tv = None
    clean_toilet = None
    wash_minor = None
    bake_cookies = None
    cold_meat = None
    help_mom = None

    def living_room(self):
        while True:
            print("===================")
            print("1)Turn on the lights\n2)Sit and watch tv\n3)Buy minecraft\n4)Clean the living room")
            print("5)Back to main menu\n===================")
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                while True:
                    user_turn = input("Turn on? (On/off): ").lower().strip()
                    if user_turn == "on":
                        print("Turned on the lights! 💡")
                        self.turn_on = True
                        if random_choice == to_do[0]:
                            if self.turn_on:
                                print("===================\nGreat!")
                                exit()
                        self.living_room()
                    elif user_turn == "off":
                        print("Lights stayed off..")
                        self.turn_on = False
                        self.living_room()
                    else:
                        print("Enter a valid choice")

            elif user_input == 2:
                user_watch = input("Watch tv? (Y/N): ").lower().strip()
                if user_watch == "y":
                    self.watch_tv = True
                    print("You watched tv you had a great time")
                    if random_choice == to_do[1]:
                        if self.watch_tv:
                            print("===================\nGreat Watching tv with the family is a good idea. 📺")
                            exit()
                    self.living_room()
                else:
                    print("===================")
                    self.living_room()

            elif user_input == 3:
                print("Buying the best game in the world is a good idea!")
                self.buy_minecraft = True
                if random_choice == to_do[2]:
                    if self.buy_minecraft:
                        print("===================")
                        print("Buying and playing the best game in the world with the family is a Great idea ⛏")
                        exit()
                self.living_room()

            elif user_input == 4:
                print("===================\nCleaning the whole living room is gonna take some time ⏳")
                print("Cleaning the living room.")
                time.sleep(5)
                print("Cleaning the living room..")
                time.sleep(5)
                print("Cleaning the living room...")
                time.sleep(5)
                print("Cleaning the living room....")
                time.sleep(5)
                print("Cleaning the living room....")
                time.sleep(5)
                print("Cleaning the living room.....")
                time.sleep(5)
                print("Done cleaning the Living room!")
                self.clean_living_room = True
                if random_choice == to_do[3]:
                    if self.clean_living_room:
                        print("===================\nCleaning is fun if you know how to do it 🧼🧹")
                        exit()
                self.living_room()
            elif user_input == 5:
                main()
            else:
                print("Enter a valid choice")

    def bathroom(self):
        while True:
            print("===================")
            print("1)Wash minor\n2)Clean the toilet\n3)Buy some toothbrush\n4)Clean the bathroom")
            print("5)Back to main menu\n===================")
            user_2 = int(input("Enter your choice: "))
            if user_2 == 1:
                print("Washing the minor.")
                time.sleep(1.34)
                print("Washing the minor..")
                time.sleep(1.34)
                print("Washing the minor...")
                time.sleep(1)
                print("Done washing the minor!")
                self.wash_minor = True
                if random_choice == to_do[5]:
                    if self.wash_minor:
                        print("Great now the minor is clean.")
                        exit()
                self.bathroom()
            elif user_2 == 2:
                print("cleaning the Toilet.")
                time.sleep(1.34)
                print("cleaning the Toilet..")
                time.sleep(1.34)
                print("cleaning the Toilet...")
                time.sleep(1)
                print("Done cleaning the Toilet!")
                self.clean_toilet = True
                if random_choice == to_do[4]:
                    if self.clean_toilet:
                        print("===================\nGreat now the Toilet is clean. 🚽")
                        exit()
                self.bathroom()

            elif user_2 == 3:
                user_bruh = input("Go to the store? (Y/N): ").lower().strip()
                if user_bruh == "y":
                    print("Nice new 🦷brushes")
                    self.buy_toothbrush = True
                    if random_choice == to_do[6]:
                        if self.buy_toothbrush:
                            print("===================\nNice lookin' brushes 😎")
                            exit()
                    self.bathroom()

            elif user_2 == 4:
                print("Cleaning the whole bathroom gonna take a lonnnnnnng time ⌚")
                print("Cleaning the Bathroom.")
                time.sleep(5)
                print("Cleaning the Bathroom..")
                time.sleep(5)
                print("Cleaning the Bathroom...")
                time.sleep(5)
                print("Cleaning the Bathroom....")
                time.sleep(5)
                print("Cleaning the Bathroom....")
                time.sleep(5)
                print("Cleaning the Bathroom...")
                time.sleep(5)
                print("Done cleaning the Bathroom!")
                self.clean_bathroom = True
                if random_choice == to_do[7]:
                    if self.clean_bathroom:
                        print("Good work cleaning the bathroom 🛀")
                        exit()
                self.bathroom()

            elif user_2 == 5:
                main()

            else:
                print("Enter a valid choice!")

    def kithen(self):
        while True:
            print("===================\n1)Make some cookies\n2)Let the Meat cool down\n3)Help mom")
            print("4)Make some Hamburgers\n5)Back to main menu\n===================")
            user_3 = int(input("Enter your choice: "))
            if user_3 == 1:
                print("You baked some cookies!")
                self.bake_cookies = True
                if random_choice == to_do[9]:
                    if self.bake_cookies:
                        print("===================\nGreat You baked some cookies for the family. 👪🍪")
                        exit()
                self.kithen()
            elif user_3 == 2:
                print("You are letting the meat cool down this will take some time..\n(30 secs)")
                time.sleep(30)
                print("Done the meat has cooled down!\n===================")
                self.cold_meat = True
                if random_choice == to_do[8]:
                    if self.cold_meat:
                        print("Yay meat :>. 🥩")
                        exit()
                self.kithen()
            elif user_3 == 3:
                print("You helped your mom to make rice!\n===================")
                self.help_mom = True
                if random_choice == to_do[10]:
                    if self.help_mom:
                        print("You and mom made the world's best rice.. 🍚♥")
                        exit()
                self.kithen()
            elif user_3 == 4:
                print("You made some Hamburger's! 🍔\n===================")
                self.make_hamburger = True
                if random_choice == to_do[11]:
                    if self.make_hamburger:
                        print("You cooked some hamburger for the family 👪🍔")
                        exit()
                    self.kithen()

            elif user_3 == 5:
                main()
            else:
                print("Enter a valid choice!")


def main():

    house1 = Home()

    try:
        while True:
            print("(To-do):", random_choice)
            print("=======================")
            print("1)Living Room\n2)Bathroom\n3)Kithen\n=======================")
            user_input = int(input("> "))

            if user_input == 1:
                house1.living_room()
            elif user_input == 2:
                house1.bathroom()
            elif user_input == 3:
                house1.kithen()
            else:
                print("Enter a valid choice!")

    except ValueError:
        print("Error!")
        main()


if __name__ == '__main__':
    main()
