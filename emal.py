from sendgrid import SendgridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='9B7bM@example.com',
    to_emails='9B7bM@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))
