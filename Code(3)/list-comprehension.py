# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)  # Output: [2, 4, 6, 8, 10]

# List comprehension with a condition
numbers = [1, 2, 3, 4, 5]
filtered = [x for x in numbers if x > 2]
print(filtered)  # Output: [3, 4, 5]


# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in matrix for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Nested dictionary comprehension
nested_dict = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print(nested_dict)  # Output: {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}
