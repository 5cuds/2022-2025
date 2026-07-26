names = ["bob", "steve", "Mary", "tom", "dicker"]
print(names[1:4])


numbers = [1, 3, 4, 5, 7, 14]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)