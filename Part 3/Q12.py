# PART 3
# Q12. Give an instruction that determines the index of the ‘@’ character
# in an email address stored in variable email_addr.

def checkValidEmail(email):
    index = email.find('@')
    if index != -1:
        print(f'@ chat found at index {index}')
    else:
        print(f'@ char not found.')

email_addr = 'abc123example.com'
checkValidEmail(email_addr)
email_addr = 'xyz123@example.com'
checkValidEmail(email_addr)
