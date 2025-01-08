# Part 4
# Q1. Write a Python program that encrypts and decrypts text files
# using a substitution cipher. Your program should ask the user for
# the name of a text file and whether they would like to encrypt or
# decrypt. Once the process is complete, you should write the output
# to a new text file with a modified name:

# This program will encrypt and decrypt text files
# Enter (e) to encrypt a password, and (d) to decrypt: e
# Enter the name of a text file to encrypt: hello.txt

# Output written to: encrypted_hello.txt
# Your program should catch exceptions and print helpful error messages.
# You should use your solution to Coding Challenge 04 to help you.

# print('This program will encrypt and decrypt text files')
# fileName = input('Enter file name: ')
# mode = input('Enter (e) to encrypt password, and (d) to decrypt: ')

def encryptFileContent(fileName):
    readFile = open(f'{fileName}.txt', 'r')
    writeFile = open(f'encrypted_{fileName}.txt','w')
    for line in readFile:
        text = line.strip()
        for char in line:
            asciiVal = ord(char)
            writeFile.write(f'{asciiVal} ')
        writeFile.write('\n')
    readFile.close()
    writeFile.close()

# def decryptedFileContent(fileName):
#     readFile = open(f'{fileName}.txt', 'r')
#     for line in

encryptFileContent('hello')
# encryptFileContent(fileName)