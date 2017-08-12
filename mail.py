import smtplib
import sys
## Constants
from_addr = "awsdocker123@gmail.com"
to_addr = "awsdocker123@gmail.com"
passwordval = "q1w2e3r4t5"
subject= "this is test mail"
message= "have a look at this msg"
def SendMail(subject, message):
  try:
    server = smtplib.SMTP('smtp.gmail.com:587')
#Next, log in to the server
    server.ehlo()
    server.starttls()
    server.login(from_addr,passwordval)
#Send the mail
    header = 'From: %s\n' % (from_addr)
    header += 'To: %s\n' % (to_addr)
    header += 'Subject: %s\n' % (subject)
    message = header + message
    server.sendmail(from_addr, to_addr, message)
    server.close()
    print "Email Sent"
    return True
  except Exception as e:
    print "Error: unable to send email.",e
    return False
SendMail(subject,message)

