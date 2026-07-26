x = 5

if x > 1:
    pass
    # raise Exception("Getting No Bitches") <| this is a user made exception

# or you can use any error not just "Exception" like TypeError, KeyError, etc..


class GreaterThenFive(Exception): # this is a user made Excption
    pass

def func():
    if x > 1:
        raise GreaterThenFive("Amount Can't Be Greater Then Five")

try:
    func()
except GreaterThenFive as e:
    print(f"Error: {e}")