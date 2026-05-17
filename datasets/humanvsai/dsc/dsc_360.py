# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Dictionary comprehension
strings = ['apple', 'banana', 'cherry']
lengths = {s: len(s) for s in strings}
print(lengths)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}

# Set comprehension
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]
unique_numbers = {n for n in numbers}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}