import random
import sys

def my_func():
    for i in range(1, 11):
        yield i


x = my_func()

#print(next(x))

# generator but in a tuple
my_TG = (i for i in range(1, 11)  if i % 2 == 0)

#for i in my_TG:
    #print(i)
print()

# countdown
def my_countdown(countdown):
    while countdown > 0:
        yield countdown
        countdown -= 1

countdown1 = my_countdown(5)

print(next(countdown1))
print()

# testing

def my_gen():
    for i in range(1, 11):
        yield random.randint(1, 10)

t = my_gen()

#for i in range(1, 11):
    #print(i + next(t))
