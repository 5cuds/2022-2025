names = ("Tom", "Bob", "Joe")
comps = ("Dell", "Apple", "Google")

zipped = zip(names, comps)

for a, b in zipped:
    print(f"{a} | {b}") # zip zip zip zip

print()


dict = dict(zip(names, comps)) # this will make a 2 tuple in to a dict

for x, y in dict.items():
    print(f"{x} | {y}")