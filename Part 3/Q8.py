# PART 3
# Give an expression that displays True if the letter ‘r’ appears in a
# given month name stored in a variable month, otherwise displays False.

def checkIfRInMonth(month):
    if 'r' in month or 'R' in month:
        print(f'{month} contains letter \'r\'')
    else:
        print(f'{month} doesn\'t contain letter \'r\'')

checkIfRInMonth('January')
checkIfRInMonth('June')
