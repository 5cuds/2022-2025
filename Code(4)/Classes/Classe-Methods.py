class MyClass:

    number = 0

    @classmethod # make a class method

    def my_method(cls, amount=50):
        cls.number = amount
        print(f"Number: {cls.number}")


MyClass.my_method()