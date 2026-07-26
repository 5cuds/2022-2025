import time
import random


def p(msg):
    print(msg)
    time.sleep(2)


class Investing:
    random_amount = random.randint(500, 5000)

    def __init__(self):
        self.amount = 0
        self.users_inv = []
        self.items = {}
        print("(===============Invest===============)\nTry to invest on random items to see")
        time.sleep(1)
        print("If they go up in prices or down\nYou have 30 days")
        time.sleep(1)
        print(f"Goal: {self.random_amount}")
        print("(====================Difficulty====================)")
        print(f"1)Easy Mode - Starting amount = 700 - Items = 24")
        print("2)Medium Mode - Starting amount = 500 - Items = 30")
        print("3)Hard Mode - Starting amount = 200 - Items = 64")
        print("====================================================")
        users_choice = int(input("> "))
        if users_choice == 1:
            self.items = {
                "notebook": 2.99, "pen": 1.49, "t-shirt": 15.99, "jeans": 39.99, "shampoo": 5.49, "soap": 1.99,
                "water bottle": 3.49, "towel": 8.99, "bedsheet": 24.99, "umbrella": 12.49, "lamp": 18.99,
                "chair": 45.99,
                "backpack": 29.99, "watch": 49.99, "headphones": 79.99, "keyboard": 25.99, "mouse": 19.99,
                "book": 12.99,
                "magazine": 4.99, "sunglasses": 14.99, "wallet": 9.99, "belt": 11.99, "gloves": 7.99, "scarf": 13.99
                }
            self.amount = 700
        elif users_choice == 2:
            self.items = {
                "notebook": 5.99, "pen": 1.49, "backpack": 39.99, "laptop": 799.99, "smartphone": 699.99,
                "headphones": 149.99, "watch": 199.99, "sunglasses": 89.99, "shoes": 59.99, "t-shirt": 14.99,
                "jeans": 49.99, "jacket": 89.99, "hat": 19.99, "gloves": 24.99, "scarf": 17.99,
                "bicycle": 299.99, "helmet": 49.99, "tent": 129.99, "sleeping bag": 89.99, "flashlight": 29.99,
                "bookshelf": 79.99, "chair": 59.99, "desk": 149.99, "lamp": 39.99, "curtains": 29.99,
                "mirror": 99.99, "picture frame": 15.99, "clock": 25.99, "wall art": 45.99, "vase": 35.99
            }
            self.amount = 500
        else:
            self.items = {
                "notebook": 5.99, "pen": 1.49, "backpack": 39.99, "laptop": 799.99, "smartphone": 699.99,
                "headphones": 149.99, "watch": 199.99, "sunglasses": 89.99, "shoes": 59.99, "t-shirt": 14.99,
                "jeans": 49.99, "jacket": 89.99, "hat": 19.99, "gloves": 24.99, "scarf": 17.99,
                "bicycle": 299.99, "helmet": 49.99, "tent": 129.99, "sleeping bag": 89.99, "flashlight": 29.99,
                "bookshelf": 79.99, "chair": 59.99, "desk": 149.99, "lamp": 39.99, "curtains": 29.99,
                "mirror": 99.99, "picture frame": 15.99, "clock": 25.99, "wall art": 45.99, "vase": 35.99,
                "washing machine": 499.99, "refrigerator": 899.99, "microwave": 99.99, "blender": 49.99,
                "toaster": 29.99,
                "vacuum cleaner": 159.99, "iron": 39.99, "fan": 45.99, "air conditioner": 299.99, "heater": 79.99,
                "shampoo": 8.99, "conditioner": 8.99, "toothpaste": 3.49, "toothbrush": 2.99, "shaving cream": 4.99,
                "hair dryer": 29.99, "hair straightener": 49.99, "nail polish": 7.99, "perfume": 59.99, "lotion": 12.99,
                "laundry detergent": 15.99, "dish soap": 2.99, "paper towels": 8.99, "trash bags": 10.99,
                "cleaning spray": 5.99,
                "batteries": 9.99, "extension cord": 14.99, "power strip": 19.99, "light bulbs": 12.99, "toolkit": 29.99
            }
            self.amount = 500
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def store(self):
        items1 = []
        count = 1
        print("==============================")
        for i in range(3):
            ran_choice = random.choice(list(self.items.keys()))
            items1.append(ran_choice)
            if self.items[ran_choice] <= 0:
                print(f"{count}) {ran_choice.capitalize()} - $FREE$")
            else:
                print(f"{count}) {ran_choice.capitalize()} - ${self.items[ran_choice]:.2f}")
            count += 1
        while True:
            buy = input("==============================\n> ").lower().strip()
            if buy in items1:
                item_price = self.items[buy]
                if item_price <= 0:
                    self.users_inv.append(buy)
                    print(f"Purchased {buy} for ${item_price:.2f}. Remaining balance: ${self.amount:.2f}")
                    return
                elif self.amount >= item_price:
                    self.users_inv.append(buy)
                    self.amount -= item_price
                    print(f"Purchased {buy} for ${item_price:.2f}. Remaining balance: ${self.amount:.2f}")
                    return
                else:
                    print("You don't have enough money to buy this item.")
                    return
            else:
                print("Enter a valid choice!")

    def show(self):
        print("==============================")
        for i in self.users_inv:
            print(f"{i.capitalize()} - ${self.items[i]:.2f}")
            time.sleep(0.30)

    def news(self):
        print("==============================")
        self.up_or_down()

    def up_or_down(self):
        amount_of_items = random.randint(1, 14)

        for i in range(amount_of_items):

            random_up = random.randint(1, 4)
            random_item = random.choice(list(self.items.keys()))
            random_price = self.items[random_item]
            times = random.randint(1, 5)
            time_ = random.randint(1, 14)

            if random_up == 1:
                upper = random_price * times
                self.items[random_item] = upper
                p(f"{random_item.capitalize()} has increased in price\n")
            elif random_up == 2:
                choice_y_n = random.randint(1, 2)
                if choice_y_n == 1:
                    upper1 = random_price * times
                    self.items[random_item] = upper1
                p(f"{random_item.capitalize()} shows signs of increasing in price\n")
            elif random_up == 3:
                upper2 = random_price - time_
                self.items[random_item] = upper2
                p(f"{random_item.capitalize()} has decreased in price\n")
            else:
                choice_y_n_ = random.randint(1, 2)
                if choice_y_n_ == 1:
                    upper3 = random_price - time_
                    self.items[random_item] = upper3
                p(f"{random_item.capitalize()} shows signs of decreasing in price\n")

    def trading(self):
        people = [
            "John Smith - 👨🏼", "Kaylee Schmidt - 👩‍🦱", "Griffin Arias - 👩🏼", "Alfredo Walton - 👦🏼",
            "Drew Cole - 👨‍", "Jay Walls - 👦️", "Jax Sosa - 👩🏾‍🦰", "Lyric Shannon - 🎵",
            "Hank McClure - 🧒🏽", "Queen Li - 👱🏽‍♀️👑",
        ]
        while True:
            items_bot = []
            ran_people = random.choice(people)
            print("==============================")
            y_n = input(f"{ran_people} Wants to trade! (Y/N): ").lower().strip()
            if y_n == "y":
                ran_amount_items = random.randint(1, 3)
                for _ in range(ran_amount_items):
                    random_item = random.choice(list(self.items.keys()))
                    items_bot.append(random_item)
                print(ran_people, end=" ")
                print(' | '.join(items_bot))
                users_trade = []
                print("==============================")
                user_8 = input("Enter a item to trade\n> ").lower().strip()
                users_trade.append(user_8)
                if user_8 == "":
                    print("Enter a item")
                    continue
                elif user_8 not in self.users_inv:
                    print("==============================")
                    print("You don't have this item in your inventory")
                    continue
                a = 1
                b = 3
                people_choice = random.randint(a, b)
                if people_choice == 1:
                    print(f"{ran_people} Accepted your trade!")
                    for jackers in items_bot:
                        self.users_inv.append(jackers)
                    print("==============================")
                    print("Items you lost:")
                    for thingers in users_trade:
                        print(thingers)
                    print("-----------------")
                    print("Items you got: ")
                    for yayers in items_bot:
                        print(yayers)
                    self.users_inv.remove(user_8)
                    users_trade.clear()
                    return
                elif people_choice == 2:
                    print("==============================")
                    print(f"{ran_people} Declined your trade..")
                    return
                else:
                    print(f"{ran_people} says that your item isn't worth his")
            else:
                print(f"Declined {ran_people} trade")
                return

    def sell(self):
        print("Type q to quit")
        print("(==========Sell==========)")
        for i in self.users_inv:
            print(f"{i.capitalize()} - ${self.items[i]}")
            time.sleep(0.30)
        while True:
            print('==============================\nType "Sell all" to sell all of the items\nType "Menu" to stop"')
            user_sell = input("Enter the item you want to sell: ").strip().lower()
            if user_sell == "menu":
                return
            elif user_sell == "sell all":
                self.amount += self.items[self.users_inv]
                self.users_inv.clear()
                print("The all of the items was sold successfully.")
            elif user_sell not in self.users_inv:
                print("You dont have the item in your inventory try again.")
                continue
            else:
                self.amount += self.items[user_sell]
                self.users_inv.remove(user_sell)
                print("The item was sold successfully.")
                continue


def main():

    i = Investing()
    days = 1
    news_times = 0

    while True:
        try:
            if i.amount == i.random_amount:
                print("You Won!")
                exit()
            elif days == 30 and i.amount != i.random_amount:
                print("You failed..")
                exit()
            elif i.amount <= 10:
                print("You Lose! You used all of your money.")
                exit()
            print("==============================")
            print(f"Day: {days}\nCurrent balance: ${i.amount:.2f}\nGoal: {i.random_amount}")
            print("==============================")
            print("1|Store\n2|Show inventory\n3|News\n4|Trading\n5|Sell items")
            print("Type 30 to pass a day")
            print("==============================")

            user_input = int(input("Enter your choice: "))

            if user_input == 1:
                i.store()
            elif user_input == 2:
                i.show()
            elif user_input == 3:
                if news_times == 1:
                    print("You can only use the news 1 time a day")
                else:
                    news_times += 1
                    i.news()
            elif user_input == 4:
                i.trading()
            elif user_input == 5:
                i.sell()
            elif user_input == 30:
                if days == 30 and i.amount != i.random_amount:
                    print("You failed..")
                    break
                else:
                    i.up_or_down()
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    news_times -= 1
                    days += 1
            else:
                print("Enter a valid choice")

        except ValueError:
            print("Error!")


if __name__ == '__main__':
    main()
