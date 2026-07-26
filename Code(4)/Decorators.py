import functools

def my_decorator(func):
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):

        print("Before the function call")
        total = func(*args, **kwargs)
        print("After the function call")

        return total
    return wrapper


@my_decorator
def double(x):
    return x * 2

total = double(5)

print(help(double))
print(double.__name__)


# 2 funcs in one
def repeat(num_times):

    def some_func(func):
        @functools.wraps(func)

        def wrapper(*args, **kwargs):

            for _ in range(num_times):

                total = func(*args, **kwargs)

            return total
        return wrapper
    return some_func


@repeat(5)
def my_func(name):
    print(f"Hello There! {name}")

# my_func("Bob")

# learn more about docorators


import functools

def ExceptionHandler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception: {e}")
    return wrapper


@ExceptionHandler
def lovely_func():
    return 342 / 0  # This will cause a ZeroDivisionError

lovely_func()
