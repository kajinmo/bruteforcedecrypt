# Brute-Force PDF Password Breaker - A program that will decrypt the PDF by trying every possible English word until it finds one that works.
# This is called a brute-force password attack. Download the text file dictionary.txt from https://nostarch.com/automatestuff2/.
# Simple password with a single english word from dictionary
# --------

import PyPDF2 as pypdf


# 1. load password list
def txt_to_list(document):
    txtfile = open(document)
    txtfile_read = txtfile.readlines()
    list_of_lists = []
    
    for line in txtfile_read:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    
    return(list_of_lists)

wordlist = txt_to_list('dictionary.txt')

# 2. iterate over password list
numbertry = 0
pdfReader = pypdf.PdfFileReader(open('encrypted.pdf', 'rb'))

if not pdfReader.isEncrypted:
    print('This file is not encrypted. You can sucessfully open it.')

else:
    for word in wordlist:
        word = str(word).strip("[']")
        trypass = str(word)
        # checking upper case
        numbertry += 1
        trypass_upper = str.upper(trypass)
        print('Trying dencryption by: {}'.format(trypass_upper))
        print('Passwords tried: ' + str(numbertry))
        result = pdfReader.decrypt(trypass_upper)
        print(result)
        if result == 1:
            print('Password found: ' + trypass_upper)
            break
        # checking lower case
        numbertry += 1
        trypass_lower = str.lower(trypass)
        print('Trying dencryption by: {}'.format(trypass_lower))
        print('Passwords tried: ' + str(numbertry))
        result = pdfReader.decrypt(trypass_lower)
        print(result)
        if result == 1:
            print('PASSWORD FOUND IN %s TRIES: %s' % (str(numbertry),trypass_lower))
            break
        continue
