# Exercise 20: Functions and Files

from sys import argv

script, input_file = argv

# Read file function
def print_all(f):
    print f.read()

# Move to file position 0
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline(),


# Open and print file
current_file = open(input_file)
print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

for current_line in range(1,4):
    print_a_line(current_line, current_file)



