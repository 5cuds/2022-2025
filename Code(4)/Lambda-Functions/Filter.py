random_words = ["Happy", "Water", "Human", "Cat", "Car", "Bottle"]

# Lambda function to check the length of the word
lambda_func = lambda x: len(x) < 5  # Keep words with length less than 5

# Use filter with the lambda function
filtered_words = filter(lambda_func, random_words)

# Convert the result to a list and print
print(list(filtered_words))
