# PART 3
# Q11. Give an instruction that determines if a given social security
# number represented as a string and stored in variable ss_num, contains
# any non-digits.

def checkSSnonDigit(ss_num):
    if ss_num.isdigit():
        print(f'{ss_num} is a digit')
    else:
        print(f'{ss_num} contains non-digits')
checkSSnonDigit('123456789')
checkSSnonDigit('123a456b789')
