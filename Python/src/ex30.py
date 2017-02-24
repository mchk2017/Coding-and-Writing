#   Exercise 30: Else and If
# ex29 in if-elif-else style
people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"
else:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"
else:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
elif people <= dogs:
    print "People are less than or equal to dogs."
else:
    print "People are dogs."

# ex30
people = 30
cars = 40
trucks = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

