# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import ssl
import os, sys

def validate_config(from_email, password) -> bool:
    if from_email == "" or from_email == None:
        return False
    if password == "" or password == None:
        return False
    
    return True


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, password, to_addrs, msg):
    #context = ssl.create_default_context()
    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    smtpobj.login(from_addr, password)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':
    FROM_ADDRESS = os.getenv("GMAIL_FROM_ADDRESS")
    MY_PASSWORD = os.getenv("GMAIL_PASSWORD")

    if len(sys.argv) < 2:
        print("Invalid argument: expected args length=2")
    TO_ADDRESS = sys.argv[1]
    BCC = ''
    SUBJECT = 'GmailのSMTPサーバ経由'
    BODY = 'pythonでメール送信'

    validate_config(FROM_ADDRESS, MY_PASSWORD) # check password and user email format

    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY

    msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
    send(FROM_ADDRESS, MY_PASSWORD, to_addr, msg)