from Modules import Car

car_1 = Car("Civic", 2019, "Honda", "Blue")
car_2 = Car("Mustang", 2021, "Ford", "Red")

def random_phone_number():
    count = 0
    max = 10
    while count < max:
        c = random.randint(0, 9)
        count += 1
        print("---------------------")
        print(f"{user_input}{c}", end="")