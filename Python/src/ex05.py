# Exercise 5: More Variables and Printing

# Variables
name = 'Paul Carroty'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d inches or %.2f cm tall." % (height, height * 2.54)
print "He's %d pounds or %.2f heavy." % (weight, weight * 453.59237)
print "Actually thah's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffe." % teeth

# tricky line
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
