numbers = [5, 7, 3, 4, 6, 2]

doubled = [i*2 for i in numbers]

print(doubled)

fruits = ["apple", "pineapple", "coconut"]

listed_fruits = [i.upper() for i in fruits]

print(listed_fruits)

grades = [90, 80, 70, 60, 50, 40, 30, 20]

graded = [i for i in grades if i >= 50]

print(graded)

print([[" " for _ in range(3)] for _ in range(3)])