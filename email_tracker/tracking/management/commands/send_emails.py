import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.management.base import BaseCommand
from decouple import config

class Command(BaseCommand):
    help = 'Send bulk emails with tracking links'

    def handle(self, *args, **kwargs):
        smtp_server = config
        port = 587
        login = config('EMAIL_HOST_USER')
        password = config('EMAIL_HOST_PASSWORD')
        recipients = ['ebubechukwu.ibeh@fewchorefinance.com', 'businesssupport@fewchorefinance.com']
        subject = 'Test Email'
        body = 'Hello, this is a test email.'

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(login, password)
        
        for recipient in recipients:
            msg = MIMEMultipart()
            msg['From'] = login
            msg['To'] = recipient
            msg['Subject'] = subject
            
            link = f"http://yourserver.com/track?email={recipient}"
            html_body = f"{body} <a href='{link}'>Click here</a>"
            msg.attach(MIMEText(html_body, 'html'))
            
            server.sendmail(login, recipient, msg.as_string())
        
        server.quit()
        self.stdout.write(self.style.SUCCESS('Successfully sent emails'))
