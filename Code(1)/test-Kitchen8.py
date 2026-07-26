import time
print("WELCOME TO THE KITCHEN!")
time.sleep(1)
print("Here you can make PIZZAS, SANDWICHES, BURGERS, FRIES, AND MORE!")
time.sleep(1)
print('''These are the ingredients:

Pizza:["Pizza dough", "Tomato sauce", "Pepperoni", "Olives", "Mozzarella cheese"],
        ["Pizza dough", "Tomato sauce", "Mozzarella cheese", "Pepper"]
        
Sandwich:["Sliced bread", "Turkey", "Cheese", "Lettuce", "Tomato slices"]

Burger:["Burger bun", "Beef patty", "Lettuce", "Tomato slices", "Cheese"],
        ["Burger bun", "Beef patty", "Lettuce", "Cheese", "fried onion rings"]
        
fries:["Potatoes", "Olive oil", "Salt", "Pepper", "Paprika",]

Hotdog:["Hotdog bun", "Hotdog sausage", "Mustard", "Ketchup"]''')
def woman():
    c = input("ingredients(1): ").capitalize()
    s = input("ingredients(2): ").capitalize()
    f = input("ingredients(3): ").capitalize()
    w = input("ingredients(4): ").capitalize()
    d = input("ingredients(5): ").capitalize()

    stuff = [c, s, f, w, d]

    burgers = [
        ["Burger bun", "Beef patty", "Lettuce", "Tomato slices", "Cheese"],
        ["Burger bun", "Beef patty", "Lettuce", "Cheese", "fried onion rings"]
    ]

    pizza_variations = [
        ["Pizza dough", "Tomato sauce", "Pepperoni", "Olives", "Mozzarella cheese"],
        ["Pizza dough", "Tomato sauce", "Mozzarella cheese", "Pepper"]
    ]

    sandwich = ["Sliced bread", "Turkey", "Cheese", "Lettuce", "Tomato slices"]

    fries=[
        ["Potatoes", "Olive oil", "Salt", "Pepper", "Paprika",]
    ]
    hotdog=[
        ["Hotdog bun", "Hotdog sausage", "Mustard", "Ketchup", "onions"]
    ]

    is_pizza = any(all(item in pizza_variation for item in stuff) for pizza_variation in pizza_variations)
    is_sandwich = all(item in sandwich for item in stuff)
    is_burger=any(all(item in burgers for item in stuff) for burger in burgers)
    is_frie=(all(item in fries for item in stuff))
    is_hotdog=all(item in hotdog for item in stuff)

    if is_pizza:
        print("You made a PIZZA! 😊🍕")
    elif is_sandwich:
        print("You made a SANDWICH! 😋🥪")
    elif is_burger:
        print("You made a BURGER! 😍🍔")
    elif is_frie:
        print("You made some FRIES! 😄🍟")
    elif is_hotdog:
        print("You made a HOTDOG! 🤤🌭")
    else:
        print("You made something else")

woman()
