# Exercise 42: Is-A, Has-A, Objects, and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has a __init__ that takes self and name parameters
        self.name = name

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has a __init__ that takes self and name parameters
        self.name = name

## class Person is-a object
class Person(object):

    def __init__(self, name):
        ## class Person has a __init__ that takes self and name parameters
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## hmm what is this strange magic?
        ## Return a proxy object that delegates method calls to a parent or sibling class of type.
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Salmon is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## sat is-a Cat
sat = Cat("Sat")

## mary is-a Person
mary = Person("Mary")

## pet attribute of mary is-a sat
mary.pet = sat

## frank is-a Employee instance
frank = Employee("Frank", 120000)

## pet attribute of frank is-a rover
frank.pet = rover

## flipper is Fish instance
flipper = Fish()

## crouse is Salmon instance
crouse = Salmon()

## harry is Halibut instance
harry = Halibut()
