class Car:
    wheels = 4
    started = False
    def __init__(self, model, year, make, color):
        self.model = model
        self.year = year
        self.make = make
        self.color = color

    def start(self):
        print(self.model, "Started...")
        self.started = True

    def stop(self):
        print(self.model, "Stopped...")
        self.started = False

    def show(self):
        if self.started:
            print(f"Model: {self.model} Year: {self.year} Make: {self.make} Color: {self.color} | Status: Started...")
        else:
            print(f"Model: {self.model} Year: {self.year} Make: {self.make} Color: {self.color} | Status: Stopped")


def main():
    while True:
        car = Car("BMW", 2025, "John Cane", "White")

        print("1)Show= Show the Model of the etc..\n2)Start = Start the car\n3)Stop = Stop the car")

        user_input = int(input("> "))
        if user_input == 1:
            car.show()
            print(f"Wheels: {car.wheels}")
        elif user_input == 2:
            car.start()
        elif user_input == 3:
            car.stop()


if __name__ == '__main__':
    main()
