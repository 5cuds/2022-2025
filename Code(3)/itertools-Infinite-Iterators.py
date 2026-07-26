import itertools

counter = itertools.count(start=10, step=2)
print(next(counter))  # 10
print(next(counter))  # 12
print(next(counter))  # 14

cycler = itertools.cycle('AB')
print(next(cycler))  # 'A'
print(next(cycler))  # 'B'
print(next(cycler))  # 'A'

repeater = itertools.repeat('Hello', 3)
print(list(repeater))  # ['Hello', 'Hello', 'Hello']
