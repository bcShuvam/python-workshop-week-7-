# PART 2
# Q4. Identify the error in the following code:
# input_file_opend = False
# while not input_file_opend:
# try: # no indentation
#     file_name = input('Enter file name: ')
#     input_file = open('file_name', 'r')
#     input_file_opned = True
# expect: print('Input file not found') # written print statement in same line