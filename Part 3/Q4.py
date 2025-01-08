# PART 3
# Q4. Write a Python function named count_letters that is given a line
# read from a text file and returns a list containing every letter in
# the line and the number of times that each letter appears
# (with upper/lower case letters counted together)
# ‘This is a line’ → [ (‘t’, 1), (‘h’, 1), (‘i’, 3), (‘s’, 2),
# (‘a’, 1), (‘l’, 1), (‘n’, 1), (‘e’, 1) ]

def count_letters(file_path):
    # Open the file and read the content
    with open(file_path, 'r') as file:
        # Initialize an empty dictionary for letter counts
        letter_counts = {}

        # Iterate through each line in the file
        for line in file:
            # Process each character in the line
            for char in line:
                char = char.lower()  # Convert to lowercase
                if char.isalpha():  # Check if the character is a letter
                    letter_counts[char] = letter_counts.get(char, 0) + 1

    # Convert the dictionary to a list of tuples and return
    return list(letter_counts.items())


# Example usage
file_path = 'Q4.txt'  # Replace with your file's path
result = count_letters(file_path)
print(result)