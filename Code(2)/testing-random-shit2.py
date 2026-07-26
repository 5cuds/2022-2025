import random
import time

clean = 100
hungry = 100
fun = 100
balance = 0.00
love = 100


class Status:

    def stat(self):

        print(f"He's love for you: {love}")
        print(f"Hungry: {hungry}")
        print(f"Fun: {fun}")
        print(f"Cleanliness: {clean}")
        print(f"Balance: ${balance}\n============================")

        user = input("Reprint? (Y/N): ").upper().strip()
        if user == "Y":
            self.stat()
        else:
            main()


class Fun:
    global clean
    global love
    global balance
    global fun

    def walk(self):
        print("You took Larry on a walk. I think she loves it!")
        self.fun += 40
        self.balance += 20
        self.love += 10
        self.clean -= 30

    def play(self):
        print("You played with Larry. Look at her she's having so much fun!")
        self.fun += 60
        self.balance += 15
        self.love += 50
        self.clean -= 20

    def toys(self):
        print("You got toys for Larry. Larry is having so much fun!")
        self.fun += 20
        self.balance += 12
        self.love += 20


class Hungry:
    global balance
    global hungry
    foods = ["pizza", "hamburger", "taco", "cat food", "hotdog", "sandwich"]

    def buy(self):
        user_2 = input("Go To Store? (Y/N): ").lower().strip()
        if user_2 == "y":
            dict_foods = {
                "pizza": 4.99,
                "hamburger": 5,
                "taco": 3,
                "hotdog": 4,
                "cat food": 8.99,
                "sandwich": 4.66
            }
            cart = []
            total = 0.00
            for food, prices in dict_foods.items():
                print(f"{food} - ${prices}")
            while True:
                print("===========================")
                user_food = input("Add Food to the cart (Show) and (Q = quit): ").lower().strip()
                if user_food in dict_foods:
                    print("Added to Cart!")
                    cart.append(user_food)
                    self.foods.append(user_food)

                    total += dict_foods[user_food]

                elif user_food == "Show":
                    print(cart)
                elif user_food == "q":
                    print("Things You got!\n", cart)
                    print(f"Total: ${total:.2f}")

                    self.balance -= total
                elif user_food not in dict_foods:
                    print("Invalid choice")

    def feed(self):
        open_or_nah = input("Open fridge? (Y/N): ").upper().strip()
        if open_or_nah == "Y":
            print(self.foods)
            user_1 = input("What Would you like to feed larry?: ").lower().strip()
            random_texts = [
                f"Larry likes That!",
                f"Larry hates that...",
                f"Larry thinks that is a bit meh but ok",
                f"it's ok.. that's what Larry said...",
                f"Larry LIKES IT SO MUCH!!"
            ]
            printer = random.choice(random_texts)
            if user_1 in self.foods:
                self.foods.remove(user_1)
                print(f"Successfully fed Larry {user_1}")
                print(printer)
                if user_1 == "pizza":
                    self.hungry += 20
                elif user_1 == "hamburger":
                    self.hungry += 50
                elif user_1 == "taco":
                    self.hungry += 15
                elif user_1 == "cat food":
                    self.hungry += 30
                elif user_1 == "hotdog":
                    self.hungry += 20
                elif user_1 == "sandwich":
                    self.hungry += 30
                main()
        else:
            main()

    def open_fridge(self):
        user_fridge = input("Open fridge(Y/N)?: ").lower().strip()
        if user_fridge == 'y':
            print("(--------Fridge--------)")
            for i in self.foods:
                print("|", i)
        else:
            main()


class Clean:
    global clean
    global balance
    global love

    if clean == 20:
        print("Larry is Really dirty Give him a bath!")
    elif clean == 0:
        print("Now Larry is REALLY DIRTY now he's sick good job..\nLATER:\nGame: larry has died from ligma...")
        print("Game Over!")
        exit()

    def bath(self):
        print("You took larry to a bath! he's lovin' it")
        print("Clean | +40\nLove | 20\nBalance | 0")
        self.clean += 40
        self.love += 20

    def pool(self):
        print("You took Larry to the pool")
        print("Clean | +50\nLove | 40\nBalance | 0")
        self.clean += 50
        self.love += 40

    def vet(self):
        print("You took larry to the vet! not sure why you needed to do that but ok")
        print("Clean | +20\nLove | 0\nBalance | -20")
        self.clean += 20
        self.love += 0
        self.balance -= 20


def main():

    global clean
    global love
    global balance
    global fun
    global hungry

    clean = Clean()
    funn = Fun()
    hungryy = Hungry()
    stat = Status()

    print("1)Clean\n2)Fun\n3)Hungry\n4)Status")
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        while True:
            user_clean = int(input("1)Bath\n2)Pool\n3)Vet\n4)Back to Main Menu\n> "))
            if user_clean == 1:
                clean.bath()
            elif user_clean == 2:
                clean.pool()
            elif user_clean == 3:
                clean.vet()
            elif user_clean == 4:
                main()
            else:
                print("Invalid choice")

    elif user_input == 2:
        while True:
            user_fun = int(input("1)Walk\n2)PLay\n3)Buy toys\n4)Back to Main Menu\n> "))
            if user_fun == 1:
                funn.walk()
            elif user_fun == 2:
                funn.play()
            elif user_fun == 3:
                funn.toys()
            elif user_fun == 4:
                main()
            else:
                print("Invalid choice")
    elif user_input == 3:
        while True:
            user_hun = int(input("1)Buy food\n2)Open fridge\n3)Feed Larry\n4)Back to Main Menu\n> "))
            if user_hun == 1:
                hungryy.buy()
            elif user_hun == 2:
                hungryy.open_fridge()
            elif user_hun == 3:
                hungryy.feed()
            elif user_hun == 4:
                main()
            else:
                print("Invalid choice")
    elif user_input == 4:
        while True:
            print("Show status?")
            user_show = input("(Y/N): ").lower().strip()
            if user_show == 'y':
                stat.stat()
            else:
                main()
    else:
        print("Enter a valid choice!")


if __name__ == '__main__':
    main()


while fun > 0:
    fun -= 1
    if fun == 70:
        print("Larry is tiny bit bored but overall doing good")
    elif fun == 50:
        print("Larry is Really bored do something like play to get outside to cheer him up!")
    elif fun == 30:
        print("OK larry is not REALLY REALLY BORED! do something!!")
    elif fun == 0:
        print("Well... larry died.. cuz of boredom (aka Fun level)")
        print("Game Over!")
        exit()
    time.sleep(0.1)

while hungry > 0:
    hungry -= 1

    if hungry == 70:
        print("Ah Larry is a bit hungry but not much really")
    elif hungry == 50:
        print("Oh no larry is hungry you should give him something to eat!")
    elif hungry == 30:
        print("Ok Larry is REALLY hungry rn You need to give him something!")
    elif hungry == 0:
        print("you have failed the game that means you failed me he died from low levels of hungry...\nGame over!")
        exit()
    time.sleep(0.1)
