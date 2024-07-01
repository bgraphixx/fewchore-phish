from django.shortcuts import HttpResponse, render
from .models import Click
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import EmailForm, UploadFileForm
from .models import Recipient

import subprocess, csv

def upload_csv_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                message = 'Error: File is not a CSV file.'
            else:
                recipients = []
                try:
                    # Process the CSV file
                    decoded_file = csv_file.read().decode('utf-8').splitlines()
                    csv_reader = csv.reader(decoded_file)
                    for row in csv_reader:
                        if row:  # Skip empty rows
                            email = row[0].strip()  # Assuming email is in the first column
                            recipients.append(email)
                            # Save recipient to the model
                            Recipient.objects.get_or_create(email=email)
                    message = f'Successfully uploaded {len(recipients)} recipients.'
                except Exception as e:
                    message = f'Error processing CSV file: {str(e)}'
                return render(request, 'upload_csv.html', {'form': form, 'recipients': recipients, 'message': message})
    else:
        form = UploadFileForm()
    return render(request, 'upload_csv.html', {'form': form})


def send_emails_view(request):
    if request.method == 'POST':
        # Run the send_emails.py script using subprocess
        try:
            subprocess.run(['python', 'manage.py', 'send_emails'], check=True)
            message = 'Emails sent successfully.'
        except subprocess.CalledProcessError as e:
            message = f'Error: {e}'
        
        return render(request, 'send_emails.html', {'message': message})
    else:
        return render(request, 'send_emails.html')


# @login_required
# def upload_recipients_view(request):
#     if request.method == 'POST':
#         form = CSVUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             csv_file = request.FILES['file']
#             decoded_file = csv_file.read().decode('utf-8').splitlines()
#             reader = csv.reader(decoded_file)
#             for row in reader:
#                 email = row[0]
#                 # Save email to your database here
#             return redirect('recipients_upload_success')
#     else:
#         form = CSVUploadForm()
#     return render(request, 'upload_recipients.html', {'form': form})

# def send_email_view(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the email message to the database
#             return redirect('email_sent_success')
#     else:
#         form = EmailForm()
#     return render(request, 'send_email.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('clicks_list')

def track_click(request):
    email = request.GET.get('email')
    if email:
        Click.objects.create(email=email)
        return HttpResponse("Thank you for clicking! You have been phished")
    return HttpResponse("Invalid request")


@login_required
def clicks_list(request):
    clicks = Click.objects.all()
    return render(request, 'click_lists.html', {'clicks': clicks})

def logout_view(request):
    logout(request)
    return redirect('login')

