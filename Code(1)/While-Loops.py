#name = input('Ender your name: ')
#while name == "":
#    print("didnt ender your name!")
#   name = input('Ender your name: ')
#print(f"hello {name}")


#age = int(input('Ender your age: '))
#while age < 5:
#    print('Age cant be below 5')
#    age = int(input('Ender your age: '))
#print(f'You are {age} years old!')


#food = input('Ender a food you like (to quit use q): ')

#while not food == "q":
#    print(f"you like {food}")
#    food = input('Ender a another food you like (to quit use Q): ')

#print('bye')


num = int(input("ender a number between 1-10: "))

while num < 1 or num > 10:
    print(f'{num} is not a valid number')
    num = int(input("ender a number between 1-10: "))

print(f'Your number is {num}')