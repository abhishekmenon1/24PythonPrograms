# You can create your program, which can help you send emails to other people.
# The program will ask your credentials and the content of the email,
# then send the data using your created command line.

import smtplib

my_email = "xxxx@gmail.com"     # Sender's Email
rec_email = "yyyy@gmail.com"    # Receiver's Email

pa = input("Whats the password: ")
password = str(pa)
msg = open('emailSample.txt', 'r')      # Opening the message text file

server = smtplib.SMTP("smtp.gmail.com", 587)    # SMTP Port 587 is used as it is secure and is commonly used
server.starttls()
server.login(my_email, password)
print("Login Successful")
server.sendmail(my_email, rec_email, msg)
server.quit()
