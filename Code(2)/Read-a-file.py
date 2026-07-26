try:
    with open('tea.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")