#from LoggingConfig import Log
#from FileManagement import FileManager
#from database import Database
#from encryption import Encryption
#from master_password import MasterPassword

import random, time
from tkinter import *

bengali_digits = {
    "0": "০",
    "1": "১",
    "2": "২",
    "3": "৩",
    "4": "৪",
    "5": "৫",
    "6": "৬",
    "7": "৭",
    "8": "৮",
    "9": "৯"
}

min_, max_ = int(input("Min: ")), int(input("Max: "))
list_of_numbers = []

while True:
      # convert
      random_number = random.randint(min_, max_)
      converted = ""
      for i in str(random_number):
            converted += bengali_digits[i]

      print(converted)
      if converted not in list_of_numbers:
            list_of_numbers.append(converted)
            print("NEW NUMBER!")

      time.sleep(5)