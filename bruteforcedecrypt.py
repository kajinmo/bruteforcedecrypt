# Brute-Force PDF Password Breaker - A program that will decrypt the PDF by trying every possible English word until it finds one that works.
# This is called a brute-force password attack. Download the text file dictionary.txt from https://nostarch.com/automatestuff2/.
# Simple password with a single english word from dictionary
# --------

import PyPDF2 as pypdf
from time import time
import os


startTime = time()
thisFolder = os.path.dirname(os.path.abspath(__file__))
txtFile = os.path.join(thisFolder, 'dictionary.txt')
pdfFile = os.path.join(thisFolder, 'encrypted.pdf')


# 1. load password list
def txtToList(document):
    txtfile = open(txtFile)
    txtfileRead = txtfile.readlines()
    list_of_lists = []
    
    for line in txtfileRead:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    
    return(list_of_lists)

wordlist = txtToList(txtFile)

# 2. iterate over password list
numberTry = 0
pdfReader = pypdf.PdfFileReader(open(pdfFile, 'rb'))

if not pdfReader.isEncrypted:
    print('This file is not encrypted. You can sucessfully open it.')

else:
    for word in wordlist:
        word = str(word).strip("[']")
        trypass = str(word)
        # checking upper case
        numberTry += 1
        tryPassUpperCase = str.upper(trypass)
        print('Trying dencryption by: {}'.format(tryPassUpperCase))
        print('Passwords tried: ' + str(numberTry))
        result = pdfReader.decrypt(tryPassUpperCase)
        if result == 1:
            print('PASSWORD FOUND IN %s TRIES: %s' % (str(numberTry), tryPassUpperCase))
            break
        # checking lower case
        numberTry += 1
        tryPassLowerCase = str.lower(trypass)
        print('Trying dencryption by: {}'.format(tryPassLowerCase))
        print('Passwords tried: ' + str(numberTry))
        result = pdfReader.decrypt(tryPassLowerCase)
        if result == 1:
            print('PASSWORD FOUND IN %s TRIES: %s' % (str(numberTry), tryPassLowerCase))
            break
        continue

endTime = time()
elapsedTime = round((endTime - startTime), 1)
print('IT TOOK %s SECONDS.' % (str(elapsedTime)))
