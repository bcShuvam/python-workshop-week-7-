# PART 3
# Q6. Give a for loop that counts all the characters in a string
# assigned to a variable line, except blanks and the newline character.

character = input('Enter any character: ')
charCount = 0

for char in character:
    if char != ' ' and char != '\n':
        charCount += 1

print(f'Total characters excluding blanks and newline: {charCount}')