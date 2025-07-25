# from mail import SendGridAPIClient
# from mail.helpers.mail import Mail
#
# message = Mail(
#     from_email='muhammadawaisidrees478@gmail.com',
#     to_emails='muhammadawaisidrees478@gmail.com',
#     subject='Test Email',
#     html_content='<strong>This is a test email sent using SendGrid and Python.</strong>'
# )
#
# try:
#     sg = SendGridAPIClient('')  # 
#     response = sg.send(message)
#     print("Email sent! Status code:", response.status_code)
# except Exception as e:
#     print("Error:", e)
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='muhammadawaisidrees478@gmail.com',
    to_emails='muhammadawaisidrees478@gmail.com',
    subject='Test Email',
    html_content='<strong>This is a test email using SendGrid</strong>'
)

try:
    sg = SendGridAPIClient('')  
    response = sg.send(message)
    print("Email sent! Status code:", response.status_code)
except Exception as e:
    print("Error:", e)
