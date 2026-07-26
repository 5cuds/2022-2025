ffood = {
    "Pizza": 6.99,
    "Hamburger": 4.99,
    "Hotdog": 1.75,
    "Taco": 3,
    "Burrito": 4.15,
    "Sandwich": 5,
    "Fries": 1.15
} 
foods = []
total = 0

for item, prices in ffood.items():
    print(f"{item} - ${prices}")
print("---------------------")

while True:
    item = input("What would you like? (Q to quit): ").capitalize()
    print("---------------------")
    if item.upper() == "Q":
        break

    elif item == "":
        print("You didn't type anything.")

    elif item not in ffood:
        print("that item is not in the list")
    else:
        while True:
            try:
                quantity = int(input("How many would you like? "))
                print("---------------------")
                if quantity < 1:
                    print("Please enter a quantity of at least 1.")
                    continue

                price = float(input("Put the price: $"))
                if price == ffood[item]:
                    print("Correct price!")
                    print("---------------------")
                    foods.append((item, quantity))
                    total += price * quantity
                    break
                else:
                    print("Wrong price! Please try again.")
            except ValueError:
                print("Please enter a valid number.")

print("(----------- YOUR ORDER -----------) ")

for food, quantity in foods:
    print(f"{quantity} x {food}")
print("---------------------")
print(f"Total: {total:.2f}")
