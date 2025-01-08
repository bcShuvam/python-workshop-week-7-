# PART 3
# Q9. Give an expression for determining how many times the letter ‘r’
# appears in a given month name stored in a variable month.

def countRinMonth(month):
    countR = 0
    for char in month:
        if 'r' in char or 'R' in char:
            countR += 1
    print(f'{month} contains {countR} \'r\'')

countRinMonth('January')
countRinMonth('June')
countRinMonth('February')