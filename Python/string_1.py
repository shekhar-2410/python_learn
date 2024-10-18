# string
str1 = "This is a string. \n This is a new line."
print(str1)

print(len(str1))

# indexing of string 
print(str1[0])

#slicing of string

# 1. Slicing a String:
text = "Hello, World!"
# Get substring from index 0 to 4 (excluding index 5)
print(text[5:len(text)])   # Output: 'Hello'

# Negative Indexing:
text = "Hello, World!"
# Slice from index -6 (W) to the end
print(text[-6:])   # Output: 'World!'

# Slicing a List:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get a slice from index 2 to 5 (excluding index 6)
print(numbers[2:6])   # Output: [2, 3, 4, 5]

# Slicing a Tuple:
tuple_data = (10, 20, 30, 40, 50, 60, 70, 80)
# Get a slice from index 1 to 4
print(tuple_data[1:5])  # Output: (20, 30, 40, 50)

# Advanced Examples:

# Reverse a List Using Slicing:
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[::-1])  # Output: [6, 5, 4, 3, 2, 1, 0]

# Extracting Odd and Even Indexed Elements:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Even-indexed elements
print(numbers[::2])  # Output: [0, 2, 4, 6, 8]

# Odd-indexed elements
print(numbers[1::2])  # Output: [1, 3, 5, 7, 9]

# Working with Multi-Dimensional Lists (2D Lists):
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Slice the first two rows and the first two columns
print([row[:2] for row in matrix[:2]])  # Output: [[1, 2], [4, 5]]

# Slicing with Default Values:
numbers = [0, 1, 2, 3, 4, 5, 6]
# Slice from index 2 to the end
print(numbers[2:])    # Output: [2, 3, 4, 5, 6]
