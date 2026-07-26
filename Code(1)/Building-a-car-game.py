command = ""
started = False
while True:

       command = input("> ").lower()
       if command == "start":
           if started:
               print("the car already started")
           else:
               started = True
               print("the car started...")
       elif command == "stop":
           if not started:
               print("The car already stopped")
           else:
               started = False
               print("the car stopped..")
       elif command == "help":
           print('''
    Start - Start the car
    stop - stop the car
    quit - quit the game''')
       elif command == "quit":
           break
       else:
           print("I don't know understand that. ")