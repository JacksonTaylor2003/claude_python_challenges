class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1

    def __str__(self):
        return f"{self.name} is {self.age} years old"

my_dog = Dog("Rex", 3)
print(my_dog.bark())      # "Rex says Woof!"
my_dog.birthday()
print(my_dog)              # "Rex is 4 years old"