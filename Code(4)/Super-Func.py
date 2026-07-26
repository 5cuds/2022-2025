class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Dog class inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class's __init__ using super()
        super().__init__(name)
        self.breed = breed

    # Override the speak method
    def speak(self):
        super().speak()  # Call the parent class's speak method
        print(f"{self.name} barks")

# Create a Dog object
dog = Dog("Buddy", "Golden Retriever")
dog.speak()
