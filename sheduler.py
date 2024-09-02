import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    sender_email = "su-23028@sitare.org"
    receiver_emails = ["su-cof2027@sitare.org"]  # List of recipient emails
    subject = "Weekly Reminder for Feedback"

    body = """
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0;">
        <p style="margin-bottom: 20px;">
            Dear Student,
        </p>
        <p style="margin-bottom: 20px;">
            Just a quick reminder to complete this week's feedback form. 
            Please submit it by the end of today otherwise you will miss the opportunity to share your thoughts for this week!
        </p>
        <p style="margin-bottom: 20px;">
            Your feedback is valuable to us.
        </p>
        <p style="margin-bottom: 20px;">
            Thank you for taking the time to provide your input!
        </p>
        <p>
            Best regards,<br>
            Feedback Management <br>
            Sitare University
        </p>
    </body>
    </html>
    """

    # Sending logic goes here

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = sender_email
    smtp_password = "cxmd uqma wvjl urie"  # Use app-specific password for security

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        
        # Send email to each recipient
        for recipient_email in receiver_emails:
            msg['To'] = recipient_email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent to {recipient_email}")
        
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Schedule the email to be sent every Monday at 10:48 AM
schedule.every().monday.at("22:52").do(send_email)

# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait a minute before checking again
