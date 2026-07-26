# Using filter with a regular function
def greater_than_three(x):
    return x > 3

numbers = [1, 2, 3, 4, 5, 6]
filtered = list(filter(greater_than_three, numbers))
print(filtered)  # Output: [4, 5, 6]

# Using filter with a lambda function
filtered_lambda = list(filter(lambda x: x > 3, numbers))
print(filtered_lambda)  # Output: [4, 5, 6]
