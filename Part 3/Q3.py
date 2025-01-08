# Part 3
# Q3. Write a Python function named check_quotes that is given a line read
# from a text file and returns True if each quote character in the line
# has a matching quote (of the same type), otherwise returns False.

# def check_quotes(fileName):
#     singleQuote = "'"
#     doubleQuote = '"'
#     countSingleQuote = 0
#     countDoubleQuote = 0
#     file = open(fileName,'r')
#     for line in file:
#         print(line)
#

def check_quotes_in_file(file_name: str):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                single_quotes = 0
                double_quotes = 0

                for i, char in enumerate(line.strip()):
                    if char == "'" and (i == 0 or line[i - 1] != '\\'):
                        single_quotes += 1
                    elif char == '"' and (i == 0 or line[i - 1] != '\\'):
                        double_quotes += 1

                # Check if quotes are properly matched
                is_matched = single_quotes % 2 == 0 and double_quotes % 2 == 0
                print(f"Line {line_number}: {is_matched}")
    except Exception as e:
        print(f"An error occurred: {e}")

check_quotes_in_file('Q3.txt')
