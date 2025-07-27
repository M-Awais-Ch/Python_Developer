# from mail import SendGridAPIClient
# from mail.helpers.mail import Mail
#
# message = Mail(
#     from_email='gmail',
#     to_emails='gmail',
#     subject='Test Email',
#     html_content='<strong>This is a test email sent using SendGrid and Python.</strong>'
# )
#
# try:
#     sg = SendGridAPIClient('sample')  #  Paste your API  here
#     response = sg.send(message)
#     print("Email sent! Status code:", response.status_code)
# except Exception as e:
#     print("Error:", e)


#email module
import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'email'
msg['From'] = 'gmail'
msg['To'] = 'gmail'
msg.set_content('hey')
# Gmail SMTP server details
smtp_server = 'smtp.gmail.com'
port = 465  # For SSL
email_address = ']gmail'
email_password = 'passw'  # Use app password, NOT your real Gmail password
# Send the email
with smtplib.SMTP_SSL(smtp_server, port) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
print("Email sent successfully!")


