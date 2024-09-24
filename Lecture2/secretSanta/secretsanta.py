# -*- coding: utf-8 -*-

import numpy as np
import random

#check that receiver and sender are always different people
def check (senders, receivers):
  for i in range(len(senders)):
    if receivers[i] == senders[i]:
      return False
  return True

#save names and emails of partecipants
receivers = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]
senders = receivers
mails = ["Alice@gmail.com", "Bob@gmail.com", "Charlie@gmail.com", "David@gmail.com", "Eve@gmail.com", "Frank@gmail.com", "Grace@gmail.com", "Heidi@gmail.com"]

myemail = "myemail@gmail.com"
mypassword = "password"

#check to see if it is all correct
print (receivers)
print (mails)

#avoid situations where the sender and the receiver are the same person
while check(senders, receivers) == False:
  random.shuffle(receivers)

#print (receivers)
#print (senders)

#send an email to the partecipants
import smtplib
from email.message import EmailMessage
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(myemail, mypassword)

for i in range(len(senders)):
  msg = EmailMessage()
  msg.set_content("Hello "+senders[i]+",\nYou have to send a gift to "+receivers[i]+".\nDon't shrink at the last moment!\nMerry Christmas and Happy New Year!\n\nSecret Santa")
  msg['Subject'] = 'Secret santa :)'
  msg['From'] = myemail
  msg['To'] = mails[i]
  server.send_message(msg)

server.quit()
