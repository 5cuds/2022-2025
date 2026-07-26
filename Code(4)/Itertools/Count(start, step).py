from itertools import count

def count(start, step):
    number = count(start, step)

    for i in number:
        print(i)

        if i == 100:
            print("Done")
            break
        
if __name__ == "__main__":
    user_input = int(input("Start: "))
    user_step = int(input("Step (Enter 1 If You Just Wanna Just Count): "))
    count(user_input, user_step)