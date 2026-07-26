from itertools import chain


numbers = [1, 2, 3]
letters = ["A", "B", "C"]

chained = chain(numbers, letters)

print(list(chained))