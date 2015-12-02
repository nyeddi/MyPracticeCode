class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name,age):
        self.name = name   # instance members
        self.age = age
    def add_trick(self, trick):
        self.tricks.append(trick)
