rows = int(input("How many rows?: "))
columns = int(input("How many Columns?: "))
symbol = input("What symbol?: ")
print("------------------")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()