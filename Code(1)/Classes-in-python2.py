class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, im {self.name}")

person1 = Person("Nihal")
person1.talk()