# user_input = input("Enter something: ")
# user_input1 = int(input("How many times?: "))
# for i in range(user_input):
#   print(user_input, number + 1)

# nums = [1, 2, 3, 4, 5]

# for num in nums:
#   if num == 3:
#        print("Three")
#        continue
#    print(num)

# for i in range(1, 11):
#     if i == 5:
#        continue
#    print(i)

successful = True

for i in range(3):
    print("Trys")
    if successful:
        print("Successful")
        break
else:
    print("Failed")