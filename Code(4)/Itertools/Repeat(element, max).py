from itertools import repeat


def main(element, max_repeats):
    repeater = repeat(element, max_repeats)

    for i in repeater:
        print(i)

if __name__ == "__main__":
    element = input("Repeat: ")
    max_repeats = int(input("Times: "))
    main(element, max_repeats)