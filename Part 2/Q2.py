# Part 2
# Q2. Create a program in Python that opens a file named 'datafile2.txt'
# for writing and assigns identifier output_file to the file object created.

output_file = open('datafile2.txt', 'w')
output_file.write('Hello World!')
output_file.close()