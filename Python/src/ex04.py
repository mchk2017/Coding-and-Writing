# Exercise 4: Variables And Names

# Define variables
cars = 100
space_in_cars = 4.0
drivers = 30
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_cars
average_passengers_per_car = passengers / cars_driven

# Print statistics for cars and passengers
print "There are", cars, "cars_available."
print "THere are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpol today."
print "We need to put about", average_passengers_per_car, "in each car."

