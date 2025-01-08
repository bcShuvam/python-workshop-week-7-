# PART 3
# Write a Python function named interleave_chars that is given two lines
# read from a text, and returns a single string containing the characters
# of each string interleaved: ‘Hello’,
# ‘Goodbye’ → ‘HGeololdobye’

def interleave_chars(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if len(lines) < 2:
        return "The file must contain at least two lines."

    line1 = lines[0].strip()
    line2 = lines[1].strip()

    interleaved = []
    max_length = max(len(line1), len(line2))
    for i in range(max_length):
        if i < len(line1):
            interleaved.append(line1[i])
        if i < len(line2):
            interleaved.append(line2[i])

    return ''.join(interleaved)

print(interleave_chars('Q5.txt'))

