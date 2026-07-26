import random
import time


# iterators are these things that iterate yeah very cool
# think of them as how for loops works but everytime
# you want to iterate you have to use the next() func

# this is how


# iterate a list
numbers = [1,2,3,4,5]

# for loop
for i in numbers:
    print(i)

print()
 
# iterator
iterate_list = iter(numbers)

# prints
print(next(iterate_list))
print(next(iterate_list))
print(next(iterate_list))
print(next(iterate_list))
print(next(iterate_list))

# very cool!

number = 4

print(isinstance(number, int))