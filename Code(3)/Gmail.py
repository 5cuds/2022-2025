import smtplib


sender = "itsngmyt@gmail.com"
receiver = "NarsandNgm@gmail.com"
password = "Nars_?!@159753"
subject = 'My first gmail to my self yay'
body = "I whote my first gmail in python!"

messsage = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, password)
server.sendmail(sender, receiver, messsage)