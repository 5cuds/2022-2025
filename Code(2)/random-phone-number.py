import random
print("Welcome To The Random Phone Number Generator!📞")
phone_code = ["+1", "+088", "+44", "+49", "+7", "+33"]
print(phone_code)
random_code = random.choice(phone_code)


def random_phone_number():
    for i in range(10):
        random_number = random.randint(1, 10)
        print(f"{random_number}", end="")


while True:
    print("---------------------------")
    user_input = input("Generate (Yes/no): ").lower()
    if user_input == "yes":
        print("-------------------")
        print(random_code, end="")
        random_phone_number()
        break
    elif user_input == "no":
        break
    else:
        print("You didn't type anything")