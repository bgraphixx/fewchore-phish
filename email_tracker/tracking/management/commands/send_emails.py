# tracking/management/commands/send_emails.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.management.base import BaseCommand
from decouple import config
from tracking.models import EmailMessage, Recipient, SignMessage
from django.conf import settings 

class Command(BaseCommand):
    help = 'Send bulk emails with tracking links'

    def handle(self, *args, **kwargs):
        smtp_server = config('EMAIL_HOST_SERVER')
        port = config('EMAIL_PORT')
        login = config('EMAIL_HOST_USER')
        password = config('EMAIL_HOST_PASSWORD')
        sender_name = config('EMAIL_SENDER')
        recipients = Recipient.objects.all().values_list('email', flat=True)

        # Fetch the latest email message
        email_message = EmailMessage.objects.latest('id')
        subject = email_message.subject
        body = email_message.message
        signature_message = SignMessage.objects.latest('id')
        signature = signature_message.message

        try: 
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(login, password)
            
            for recipient in recipients:
                msg = MIMEMultipart()
                msg['From'] = msg['From'] = f'{sender_name} <{login}>'
                msg['To'] = recipient
                msg['Subject'] = subject

                domain = settings.ALLOWED_HOSTS[0]
                link = f"http://{domain}/vote?email={recipient}"
                html_body = f"{body} <a href='{link}'>VOTE NOW</a> <p>Thank you for your cooperation</p> {signature}"
                msg.attach(MIMEText(html_body, 'html'))

                
                
                server.sendmail(login, recipient, msg.as_string())
            
            server.quit()
            self.stdout.write(self.style.SUCCESS('Successfully sent emails'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to send emails: {str(e)}'))
