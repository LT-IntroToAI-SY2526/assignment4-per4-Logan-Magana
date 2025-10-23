# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:


#  a simple dog class to learn OOP concepts
# breed-breed of the dog
# fur_color- the fur color of dog
# name- name of dog 

    def __init__(self, breed, fur_color, name, age):
        """Initialize a new Dog with breed, fur_color, name and age"""
        self.breed = breed
        self.fur_color = fur_color
        self.name = name
        self.age = age

    def __str__(self):
        """String representation of a dog"""
        return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}"
    def bark(self):
        return( f" {self.name} says: Woof Woof " )
if __name__ == "__main__":
    berg_dog = Dog("labrador", "black", "logan", 9)
    aidan_dog = Dog("lab pitt mix", "grey", "cubbie", 9)
    print(aidan_dog.bark())