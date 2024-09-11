import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    sender_email = "kpuneet474@gmail.com"
    # receiver_emails = ["su-cof2027@sitare.org"]  # List of recipient emails
    receiver_emails = ["su-cof2026@sitare.org"]  # List of recipient emails
    subject = "Weekly Reminder for feedback"
    body = "All students, please fill the feedback for all subjects."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = sender_email
    smtp_password = "jyrj qnay shxz cfov"  # Use app-specific password for security

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
schedule.every().monday.at("11:21").do(send_email)

# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait a minute before checking again
