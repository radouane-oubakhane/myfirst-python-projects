import smtplib

sender = "sender@gmail.com"
recever = "recever@gmail-com"
password ="password123"
subject = "Python email test"
body = "I wrote an email! :D"
message = f"""From: {sender}
To: {recever}
Subject: {subject}\n
{body}
"""
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
try:
    server.login(sender,password)
    print("Loged in...")
    server.sendmail(sender,recever,message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")
