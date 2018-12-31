# Import smpt library
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

frommail = input("Enter From Address: ")
tomail = input("Enter To Address: ")
mailsubject = input("Enter Email Subject: ")

# Open text file for body of email
fp = open('c:\\scripts\\body', 'r')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# set to and from of email
msg['Subject'] = mailsubject
msg['From'] = frommail
msg['To'] = tomail

# send email out via local smtp server
s = smtplib.SMTP('localhost')
s.sendmail(frommail, [tomail], msg.as_string())
s.quit()
