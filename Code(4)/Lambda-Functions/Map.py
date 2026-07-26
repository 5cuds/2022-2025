random_numbers = [5, 7, 5, 1, 2, 7]

mapped = map(lambda x: x * x, random_numbers)

print(list(mapped))

lc_way = [x*x for x in random_numbers]

print(lc_way)