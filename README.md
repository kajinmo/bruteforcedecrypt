# bruteforcedecrypt

A program that will decrypt the PDF by trying every possible English word until it finds one that works. This is called a brute-force password attack.

This is a pratical project for educational use from the book "Automate the Boring Stuff with Python".

The program try to find a simple password with a single english word from dictionary. The text file dictionary.txt can be downloaded from https://nostarch.com/automatestuff2/. This dictionary file contains over 44,000 English words with one word per line.

Here’s what the program will do:
1. Using the file-reading, create a list of word strings by reading this file.
2. Then loop over each word in this list, passing it to the decrypt() method.
3. If this method returns the integer 0, the password was wrong and your program should continue to the next password. If decrypt() returns 1, then your program should break out of the loop and print the hacked password. The program must try both the uppercase and lowercase form of each word.
