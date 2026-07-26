import smtplib
from email.message import EmailMessage


def send_email(subject, body, to_emails):
    # Outlook account credentials
    email_address = 'ngmandnars@outlook.com'
    email_password = '1;+1Q|~H/BV($9<@Xg3MzE)++ctN'  # Use an app password if you have 2FA enabled

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to_emails  # Join multiple emails with commas
    msg.set_content(body)

    # Connect to the Outlook SMTP server
    with smtplib.SMTP('smtp.office365.com', 587) as smtp:
        smtp.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        smtp.login(email_address, email_password)  # Log in to the email account
        smtp.send_message(msg)  # Send the email

# Usage
send_email('Test Subject', 'This is the body of the email.', "NarsAndNgm@gmail.com")
