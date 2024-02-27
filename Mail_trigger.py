import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up your Gmail credentials
email_address = 'tejasmg007@gmail.com'
password = 'ckqa vgjb fmbl lmvp'  # Generate this in your Google Account settings

# Set up the email content
subject = 'Test Trigger'
body = 'its working perfectly'

# Create the MIME object
message = MIMEMultipart()
message['From'] = email_address
message['To'] = 'siddeshmg007@gmail.com'
message['Subject'] = subject

# Attach the body to the email
message.attach(MIMEText(body, 'plain'))

# Connect to the Gmail SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    # Start TLS for security
    server.starttls()
    
    # Log in to your Gmail account
    server.login(email_address, password)
    
    # Send the email
    server.sendmail(email_address, 'siddeshmg007@gmail.com', message.as_string())

print('Email sent successfully!')