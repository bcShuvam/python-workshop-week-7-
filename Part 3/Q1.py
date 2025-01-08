# PART 3
# Q1.Write a Python function called reduce_spaces that is given a 
# line read from a text file and returns the line with all extra space 
# characters removed:
# ‘This line has extra space characters’ → 
# ’This line has extra      space characters’

def reduce_spaces(fileName):
    file = open(f'{fileName}.txt','r')
    return ' '.join(file.read().split()) # splits the string and then joins it

line = 'This line has extra      space characters'

print(reduce_spaces('Q1'))

