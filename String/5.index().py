# Example: Using index() method with strings

# The index() method finds the position of the first occurrence of a substring
# Syntax: string.index(substring, start, end)
# - substring: what we want to find
# - start: optional, index to start searching from
# - end: optional, index to stop searching

text = "Hello world"

# Find the index of the first "o"
first_o = text.index("o")  # "o" first appears at index 4
print("The first 'o' is at index:", first_o)

# Find the index of "o" starting from index 5
second_o = text.index("o", 5)  # starts searching after index 5
print("The next 'o' after index 5 is at:", second_o)

# If the substring does not exist, index() will raise a ValueError
# For example, searching for "z" will cause an error
# Uncommenting the following line will raise an error
# text.index("z")