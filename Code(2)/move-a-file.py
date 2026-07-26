import os.path

file = "tea.txt"
pro = "C:\\Users\\Windows\\Documents\\tea.txt"
try:
    if os.path.exists(pro):
        print("This file is been always there ")
    else:
        os.replace(file, pro)
except FileNotFoundError:
    print("No file was found")