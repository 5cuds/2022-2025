import time


class TDList:

    def __init__(self) -> None:
        self.tb_lists = []
        self.done = []


    def add_list(self):

        user_input = input("=================\nEnter A To-Do-List:\n")
        self.tb_lists.append(user_input)

        print("List Added!")

    
    def show_list(self):
        print()
        for i in self.tb_lists:

            time.sleep(0.25)
            print(i.title() + "\n")


    def show_done(self):
        print()
        for i in self.done:

            time.sleep(0.25)
            print(i.title( ) + "\n")


    def delete_list(self):
        for i, element in enumerate(self.tb_lists):

            time.sleep(0.25)
            print(f"{i}) {element}\n")

        user_input = int(input("\n=================\nEnter The Index Of The List To Delete It.\nEnter: "))

        self.done.append(self.tb_lists[user_input])
        self.tb_lists.remove(self.tb_lists[user_input])

        print("=================\nDeleting..\n")
        time.sleep(2)
        print("Deleted The List!")
    

def main():
    e = TDList()
    while True:
        try:
            print("=================\n1)Add A List\n2)Delete A List\n3)Done Lists\n4)Show List")
            user = input("=================\n> ")
            if user == "1":
                e.add_list()
            elif user == "2":
                e.delete_list()
            elif user == "3":
                e.show_done()
            else:
                e.show_list()
        except ValueError as ee:
            print(f"=================\nError: {ee}")
if __name__ == "__main__":
    main()