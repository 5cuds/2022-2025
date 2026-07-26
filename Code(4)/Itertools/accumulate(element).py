from itertools import accumulate

list_numbers = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]

numbed = accumulate(list_numbers)

print(list(numbed))