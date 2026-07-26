import os

source = "tea.txt"
destinnetin = "C:\\Users\\Windows\\Documents\\tea.txt"
try:
    if os.path.exists(destinnetin):
        print("That file is there")
    else:
        os.replace(source, destinnetin)
        print(f"{source} was moved")
except FileNotFoundError:
    print("The file was not found")