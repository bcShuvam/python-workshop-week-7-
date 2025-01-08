# PART 2
# Q3. Assume that input_file is a file object for a text file open for
# reading, and output_file is a file object for a text file open for writing.
# Explain the contents of the output after the following code terminates:

empty_str = ''
line = input_file.readline()
while line != empty_str:
    output_file.write(line + '\n')
        line = input file.readline()