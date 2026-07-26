while True:
    name=input("Ender Your name: ")
    if name == "":
        print("You didn't ender your name!")
    if name != "":
        print(f"Hello {name}")
        break

num = input("Ender your Phone number: ")
if num == "":
    print("You didn't ender you phone number!")
    num = input("Ender your Phone number: ")
    num = input("Ender your Phone number(one more try..): ")
for i in num:
    if i == "-":
        continue
    print(i, end="")


import time
print(".")
time.sleep(0.45)
print("..")
time.sleep(0.45)
print("...")
time.sleep(0.45)
print("haha i got you phone number and your name haha")