# dictionary =  a collection of {key:value} pairs
#                       ordered and changeable. No duplicates

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}
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

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#   print(key)

# values = capitals.values()
# for value in capitals.values():
# print(value)

# items = capitals.items()
# for key, value in capitals.items():
#    print(f"{key}: {value}")