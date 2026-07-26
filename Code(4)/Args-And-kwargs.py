listOfNames = []

def add_names(*args): # args is a aumt thats takes inf amount of aumts
    for i in args:
        listOfNames.append(i)

print(f"Old List: {listOfNames}")
add_names("Tom", "Steve", "Mary", "Mosh", "Bob")
print(f"New List: {listOfNames}")


def sumitup(*args):
    # total = 0
    # for i in args:
        # total += i
    # print(f"\nTotal: {total}") or

    print(f"\nTotal: {sum(args)}")

sumitup(4, 2, 5, 9, 6)


def person(**ks):
    print(f"\nName: {ks["name"]}\nJob: {ks["job"]}\nIncome: {ks["income"]}")


person(name="Bob", job="Google", income=50000)