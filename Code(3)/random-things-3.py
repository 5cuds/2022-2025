def my_der(func):
    def wrapper():
        print("Hello there")
        func()
        print("Im Dickerson")
    return wrapper

@my_der
def hello():
    print("Good to see you!")


hello()