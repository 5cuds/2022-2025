# Basic lambda function
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Using lambda within a higher-order function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]
