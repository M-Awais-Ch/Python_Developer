import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'email'
msg['From'] = 'muhammadawaisidrees478@gmail.com'
msg['To'] = 'awaisidrees478@gmail.com'
msg.set_content('Successfuly Send mail')
smtp_server = 'smtp.gmail.com'
port = 465
email_address = 'muhammadawaisidrees478@gmail.com'
email_password = 'yyzc iyxc endy puhm'
with smtplib.SMTP_SSL(smtp_server, port) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
print("Email sent successfully done!")