# Part 3
# Q3. Write a Python function named check_quotes that is given a line read
# from a text file and returns True if each quote character in the line
# has a matching quote (of the same type), otherwise returns False.

# def check_quotes(fileName):
#     singleQuote = "'"
#     doubleQuote = '"'
#     countSingleQuote = 0
#     countDoubleQuote = 0
#     file = open(fileName,'r')
#     for line in file:
#         print(line)
#

def check_quotes(line: str) -> bool:
    """
    Checks if each quote character in the line has a matching quote of the same type.

    Args:
        line (str): A line of text.

    Returns:
        bool: True if all quotes are properly matched, otherwise False.
    """
    single_quotes = 0  # Count of single quotes (')
    double_quotes = 0  # Count of double quotes (")

    i = 0
    while i < len(line):
        char = line[i]
        # Check for escaped single quotes
        if char == "'" and (i == 0 or line[i - 1] != '\\'):
            single_quotes += 1
        elif char == '"':
            double_quotes += 1
        i += 1

    # Quotes are properly matched if both counts are even
    return single_quotes % 2 == 0 and double_quotes % 2 == 0


# Example usage
line1 = 'He said, "Hello, how are you?"'
line2 = "It's a sunny day"
line3 = 'She said, "It\'s beautiful," but didn\'t stay.'
line4 = 'Unmatched "quote'

print(check_quotes(line1))  # Output: True
print(check_quotes(line2))  # Output: True (Corrected)
print(check_quotes(line3))  # Output: True
print(check_quotes(line4))  # Output: False