# PART 3
# Write a Python function named interleave_chars that is given two lines
# read from a text, and returns a single string containing the characters
# of each string interleaved: ‘Hello’,
# ‘Goodbye’ → ‘HGeololdobye’

def interleave_chars_from_file(file_path):
    # Open the file and read its content
    with open(file_path, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Ensure the file has at least two lines
    if len(lines) < 2:
        return "The file must contain at least two lines."

    # Get the first two lines and strip any trailing newline characters
    line1 = lines[0].strip()
    line2 = lines[1].strip()

    # Interleave the characters from the two lines
    interleaved = []
    max_length = max(len(line1), len(line2))
    for i in range(max_length):
        if i < len(line1):
            interleaved.append(line1[i])
        if i < len(line2):
            interleaved.append(line2[i])

    # Return the interleaved string
    return ''.join(interleaved)


# Example usage
file_path = 'Q5.txt'  # Replace with the path to your file
result = interleave_chars_from_file(file_path)
print(result)
