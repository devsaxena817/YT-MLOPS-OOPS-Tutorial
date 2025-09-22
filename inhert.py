# Simple inheritance

# # Base class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # # # Derived class
# class Dog(Animal):
#     # def __init__(self):
#     #     self.behaviour ="Friendly"

#     def speak1(self):
#         print(f" IT barks.He is very {self.behaviour}.")

# # # # Create an instance of Animal
# animal = Animal("Generic Animal")
# animal.speak()  # Output: Generic Animal makes a sound.

# # # # Create an instance of Dog
# dog = Dog("Buddy")
# dog.speak()  # Output: Buddy barks.


# Super Keyword

# Super

# Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# # # Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()  # Call the base class method
        print(f"{self.name} barks. It is a {self.breed}.")

# # # Create an instance of Dog
dog = Dog("Golden Retriever")
dog.speak()
# Output:
# Buddy makes a sound.
# Buddy barks. It is a Golden Retriever.