# automatic email sender
# file organizer
# number gusseing game


# projects
# smtp protocol
# os (lib)
# while again
# ranint (function)

import smtplib


sender='@gmail.com'
password=''
reciever=''



s = smtplib.SMTP('smtp.gmail.com', 587)
# to tell about the gmail server


s.starttls()

# tls certificates msg encryted



s.login(sender, password)


# authenticate
message = ("Hello, this is a test email. kese ho")



for x in range(2):
    print("Email: sending")
    s.sendmail(sender,reciever,message)
    print('email has been sent')


s.quit()