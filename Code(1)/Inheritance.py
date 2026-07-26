class Cat:
    def walk(self):
        print("Walk")

class Dog(Cat):
    def Bark(self):
        print("Bark!")

class Cow(Cat):
    def moo(self):
        print("Moo!!")

dog=Cow()
dog.moo()
