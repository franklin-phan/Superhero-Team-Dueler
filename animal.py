class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        "{} is eating.".format(self.name)
    def drink(self):
        "{} is drinking. ".format(self.name)