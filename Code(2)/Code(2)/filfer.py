frds = [
    ("Steve", 16),
    ("May", 14),
    ("Jack", 19),
    ("Johnson", 18),
    ("Tommy", 17),
    ("Cole", 19),
    ("Tim", 14)
]

ages = lambda x: x[1] >= 18

adults = list(filter(ages, frds))

for i in adults:
    print(i)