from collections import namedtuple

Point = namedtuple("Point", "x,y") # make a class field

pt = Point(1, -4) # set aumts

print(pt.x * 2) # use it with something

print()

Person = namedtuple("Name", "name,job,income") # Make a Person Class

person_1 = Person("Bob", "Google", 50000) # Make a person
person_2 = Person("Mary", "Apple", 100000) # you can use it many times as you want

print(f"Person - 1\n---------------\nName: {person_1.name}\nJob: {person_1.job}\nIncome: ${person_1.income}\n")
print(f"Person - 2\n---------------\nName: {person_2.name}\nJob: {person_2.job}\nIncome: ${person_2.income}")

