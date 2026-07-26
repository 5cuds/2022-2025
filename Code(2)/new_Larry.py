import random
import time
import threading

# Global stats
clean = 100
hungry = 100
fun = 100
balance = 50.00
love = 100
game_over = False

def print_status():
    print(f"\n============================")
    print(f"Larry's Stats:")
    print(f"  Love:         {love}")
    print(f"  Hungry:       {hungry}")
    print(f"  Fun:          {fun}")
    print(f"  Cleanliness:  {clean}")
    print(f"  Balance:      ${balance:.2f}")
    print(f"============================\n")

# ---- FOOD SHOP ----
fridge = ["cat food"]

dict_foods = {
    "pizza": 4.99,
    "hamburger": 5.00,
    "taco": 3.00,
    "hotdog": 4.00,
    "cat food": 8.99,
    "sandwich": 4.66
}

food_hunger = {
    "pizza": 20,
    "hamburger": 50,
    "taco": 15,
    "cat food": 30,
    "hotdog": 20,
    "sandwich": 30
}

def go_shopping():
    global balance
    print("\n(-------- STORE --------)")
    for food, price in dict_foods.items():
        print(f"  {food} - ${price:.2f}")
    cart = []
    total = 0.0
    while True:
        print("============================")
        user_food = input("Add food to cart (or 'show' / 'done'): ").lower().strip()
        if user_food == "done":
            if cart:
                print(f"\nYou bought: {cart}")
                print(f"Total: ${total:.2f}")
                if total > balance:
                    print("You don't have enough money!")
                else:
                    balance -= total
                    fridge.extend(cart)
                    print("Added to fridge!")
            break
        elif user_food == "show":
            print(f"Cart: {cart} | Total: ${total:.2f}")
        elif user_food in dict_foods:
            cart.append(user_food)
            total += dict_foods[user_food]
            print(f"Added {user_food} to cart!")
        else:
            print("That item isn't in the store.")

def feed_larry():
    global hungry, love
    if not fridge:
        print("The fridge is empty! Go shopping first.")
        return
    print(f"\nFridge: {fridge}")
    user_1 = input("What would you like to feed Larry?: ").lower().strip()
    random_texts = [
        "Larry likes that!",
        "Larry hates that...",
        "Larry thinks that is a bit meh but ok",
        "It's ok... that's what Larry said...",
        "Larry LIKES IT SO MUCH!!"
    ]
    if user_1 in fridge:
        fridge.remove(user_1)
        print(f"Successfully fed Larry {user_1}!")
        print(random.choice(random_texts))
        hungry = min(100, hungry + food_hunger.get(user_1, 10))
        love = min(100, love + 5)
    else:
        print("That's not in the fridge!")

# ---- FUN ----
def take_walk():
    global fun, love, clean, balance
    print("You took Larry on a walk. She loves it!")
    fun = min(100, fun + 40)
    balance += 20
    love = min(100, love + 10)
    clean = max(0, clean - 30)

def play_with_larry():
    global fun, love, clean
    print("You played with Larry. Look at her go!")
    fun = min(100, fun + 60)
    love = min(100, love + 50)
    clean = max(0, clean - 20)

def give_toys():
    global fun, love, balance
    print("You got toys for Larry. She's having so much fun!")
    fun = min(100, fun + 20)
    love = min(100, love + 20)
    balance = max(0, balance - 12)

# ---- CLEANLINESS ----
def give_bath():
    global clean, love
    print("You gave Larry a bath! She loves it!")
    print("Clean | +40  Love | +20")
    clean = min(100, clean + 40)
    love = min(100, love + 20)

def take_to_pool():
    global clean, love
    print("You took Larry to the pool!")
    print("Clean | +50  Love | +40")
    clean = min(100, clean + 50)
    love = min(100, love + 40)

def take_to_vet():
    global clean, love, balance
    print("You took Larry to the vet!")
    print("Clean | +20  Balance | -20")
    clean = min(100, clean + 20)
    balance = max(0, balance - 20)

# ---- STAT DECAY (runs in background) ----
def stat_decay():
    global fun, hungry, clean, game_over
    while not game_over:
        time.sleep(15)
        if game_over:
            break
        fun = max(0, fun - 5)
        hungry = max(0, hungry - 5)
        clean = max(0, clean - 3)

        if fun == 0:
            print("\nLarry died of boredom... Game Over!")
            game_over = True
        elif hungry == 0:
            print("\nYou failed Larry... she died from hunger. Game Over!")
            game_over = True
        elif clean == 0:
            print("\nLarry got sick from being too dirty... Game Over!")
            game_over = True
        elif fun <= 30:
            print("\n⚠️  Larry is REALLY bored! Do something!")
        elif hungry <= 30:
            print("\n⚠️  Larry is REALLY hungry! Feed her!")
        elif clean <= 30:
            print("\n⚠️  Larry is really dirty! Give her a bath!")

# ---- MAIN MENU ----
def main():
    global game_over

    print("🐱 Welcome to Cat-Larry! 🐱")
    print("Larry is your new cat. Keep her happy!\n")
    print_status()

    decay_thread = threading.Thread(target=stat_decay, daemon=True)
    decay_thread.start()

    while not game_over:
        print("\nWhat would you like to do?")
        print("  1) Check Stats")
        print("  2) Feed Larry")
        print("  3) Go Shopping")
        print("  4) Play with Larry")
        print("  5) Take a Walk")
        print("  6) Give Toys")
        print("  7) Give Bath")
        print("  8) Take to Pool")
        print("  9) Take to Vet")
        print("  Q) Quit")

        choice = input("\n> ").strip().upper()

        if choice == "1":
            print_status()
        elif choice == "2":
            feed_larry()
        elif choice == "3":
            go_shopping()
        elif choice == "4":
            play_with_larry()
        elif choice == "5":
            take_walk()
        elif choice == "6":
            give_toys()
        elif choice == "7":
            give_bath()
        elif choice == "8":
            take_to_pool()
        elif choice == "9":
            take_to_vet()
        elif choice == "Q":
            print("Goodbye! Larry will miss you 🐱")
            game_over = True
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
