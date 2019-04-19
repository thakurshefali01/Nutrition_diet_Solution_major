import smtplib

import os
from email.mime.multipart import MIMEMultipart #MImemultipart== attachment,body
from email.mime.text import MIMEText

def otpsend(otp,useremail,subject,message):
    try:
        msg = MIMEMultipart()
        msg['From'] = 'thakurshefali53@gmail.com'
        msg['To'] = useremail
        msg['subject'] = subject

        body = message+"your one time password is ="+str(otp)
        msg.attach(MIMEText(body, "plain"))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('thakurshefali53@gmail.com', 'thakurshefali01')
        text = msg.as_string()
        server.sendmail(msg["From"], msg["To"], text)
        server.quit()
        return True,"otp sent"
    except:
        return False,"something went wrong"


def email(emailid,subject,message):
        msg = MIMEMultipart()
        msg['From'] = 'thakurshefali53@gmail.com'
        msg['To'] = emailid
        msg['subject'] = subject

        body = message
        msg.attach(MIMEText(body, "plain"))
        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login('thakurshefali53@gmail.com', 'thakurshefali01')

        text = msg.as_string()
        server.sendmail(msg["From"], msg["To"], text)
        server.quit()
