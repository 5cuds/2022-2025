import re

# Example string
string = "I spent 250 on Food and 150 on Fuel."

# Find the first number in the string
match = re.search(r'\d+', string)

# Check if a match was found and print the result
if match:
    first_number = int(match.group())
    print(first_number)  # Output: 250
