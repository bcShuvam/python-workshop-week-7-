# PART 3
# Q14. For a variable named err_mesg that contains error messages
# in the form ** error message **, give an expression that produces
# a string containing the error message without the leading and
# trailing asterisks and blank characters.

errMsg = '** error message **'
removedStars = errMsg.replace('*', '')
print(removedStars.strip())