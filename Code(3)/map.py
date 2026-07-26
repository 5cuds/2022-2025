# Using map with a regular function
def add_five(x):
    return x + 5

numbers = [1, 2, 3, 4, 5]
result = list(map(add_five, numbers))
print(result)  # Output: [6, 7, 8, 9, 10]

# Using map with a lambda function
result_lambda = list(map(lambda x: x + 5, numbers))
print(result_lambda)  # Output: [6, 7, 8, 9, 10]


class Person:
    def __init__(self, name):
        self.name = name

def greet(person):
    return f"Hello, {person.name}!"

people = [Person("Alice"), Person("Bob")]
greetings = map(greet, people)
print(list(greetings))
