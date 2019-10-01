class Dog:
    def __init__(self, name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Wolf!")
    def sit(self):
        print("<>sits")
    def roll_over(self):
        print("<> rolls over")

my_dog = Dog("Rex","SuperDog")
Dog.greeting = "Woah"