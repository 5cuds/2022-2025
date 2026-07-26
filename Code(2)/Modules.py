class Car:
        wheels = 4

        def __init__(self, model, year, make, color):
            self.model = model
            self.year = 2022
            self.make = make
            self.color = color

        def start(self):
            print(f"{self.model} started...")

        def stop(self):
            print(f"{self.model} stopped...")