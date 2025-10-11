import smtplib  
from email.message import EmailMessage  

def send_email(to, subject, body):  
    email = EmailMessage()  
    email['From'] = 'your_email@example.com'  
    email['To'] = to  
    email['Subject'] = subject  
    email.set_content(body)  

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  
        smtp.login('your_email@example.com', 'your_app_password')  
        smtp.send_message(email)  

# Example usage  
send_email('receiver@example.com', 'Test Subject', 'Hello, this is a test email!')