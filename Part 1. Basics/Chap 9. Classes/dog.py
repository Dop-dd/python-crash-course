class Dog:
    # model a dog
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        # simulate a dog sitting down
        print(f"{self.name} is sitting")

    def roll_over(self):
        print(f"{self.name} is rolling over")

# make an instance representing a specific dog

my_dog = Dog('willo', 6)
print(f"my dog's name is {my_dog.name}")
print(f"my dog's is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()