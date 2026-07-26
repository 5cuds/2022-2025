
import time
import datetime


date = datetime.date.today()

time = datetime.datetime.now().strftime("Time: %H:%M:%S\nDate: %m-%d-%Y")

print(time)