import secrets

a = secrets.randbelow(10) # it kinda like randint() but it doesnt pick the number that was given also like randrange
print(a)

b = secrets.randbits(4) # it picks binary
print(b)

my_list = [5, 4, 7, 8, 6, 2]
c = secrets.choice(my_list) # is also like choice() in the random module but is not reproducible
print(c)

# B t w learn numpy - Old Nihal