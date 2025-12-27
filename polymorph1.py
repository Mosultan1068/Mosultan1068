class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Parrot:
    def speak(self):
        return "Ho Ho Hi I am the parrot."

# Polymorphism in action
def make_animal_speak(animal):
        print(animal.speak())


# Different objects, same interface
dog = Dog()
cat = Cat()
parrot = Parrot()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!
make_animal_speak(parrot)
