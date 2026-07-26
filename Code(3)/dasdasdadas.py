from functools import total_ordering


def test(*args):
    total = 0
    for i in args:
        total += i
    return total

print(test(2, 2))