#try:
#    age = int(input("What's is your age?: "))
#    print(f"Your {age} years old")
#except ValueError:
 #   print("something gone wrong")


try:
    age = int(input("What's is your age?: "))
    income=20000
    risk= income / age
    print(f"Your {age} years old")
except ZeroDivisionError:
    print("age cant not be 0")
except ValueError:
    print("something gone wrong")