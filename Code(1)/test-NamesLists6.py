names = [
    'Bob',
    'Mike',
    'steve'
]
length = {name:len(names) for name in names}
print(length)


user_input = input("(Name): ")

name = user_input or "N/A"