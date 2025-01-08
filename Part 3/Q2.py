# Part 3
# Q2. Write a Python function named extract_temp that is given a 
# line read from a text file and displays the one number (integer) 
# found in the string:
# ’The high today will be 75 degrees’ → 75.
import re

file_name = 'Q2.txt'

def extract_temp(file):
    with open(file, 'r') as file:
        for line in file:
            print(line)
            result = re.search(r'\b\d+', line)
            if result:
                print(result.group())
            else:
                print("No integer found in this line.")

extract_temp(file_name)
