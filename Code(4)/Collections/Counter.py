from collections import Counter

chars = "abaaacccbbbccacacacacacbcbbbcbbcbcbbbbbbbccc"

my_counter = Counter(chars)

for i, y in my_counter.items(): # counts how many chars are in the list
    print(f"{i.upper()} - {y}")

print()
print(f"Most Common Char: {my_counter.most_common(1)[0][0]}\n") # finds the most common char in the list
                                                            # You can also put 2, 3, etc to find the 2st most common