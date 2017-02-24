# Exercise 15: Reading Files
from sys import argv

# Setup a script- and name of file
script, filename = argv

# Open file
txt = open(filename)

# Read file
print "Here's your file %r:" % filename
print txt.read()

# Read file from filename
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

# Print file
print txt_again.read()

