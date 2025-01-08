# PART 3
# Q4. Write a Python function named count_letters that is given a line
# read from a text file and returns a list containing every letter in
# the line and the number of times that each letter appears
# (with upper/lower case letters counted together)
# ‘This is a line’ → [ (‘t’, 1), (‘h’, 1), (‘i’, 3), (‘s’, 2),
# (‘a’, 1), (‘l’, 1), (‘n’, 1), (‘e’, 1) ]

def count_letters(file_path):
    with open(file_path, 'r') as file:
        letter_counts = {}

        for line in file:
            for char in line:
                char = char.lower()
                if char.isalpha():
                    letter_counts[char] = letter_counts.get(char, 0) + 1

    return list(letter_counts.items())

print(count_letters('Q4.txt'))

