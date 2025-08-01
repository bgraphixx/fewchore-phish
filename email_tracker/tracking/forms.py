# tracking/forms.py
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import EmailMessage, SignMessage


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = ['subject', 'message']
        widgets = {
            'message': CKEditorWidget(),
        }


class SignForm(forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = ['subject', 'message']
        widgets = {
            'message': CKEditorWidget(),
        }



class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a CSV file')