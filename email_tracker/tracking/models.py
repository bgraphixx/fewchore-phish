from django.db import models
from ckeditor.fields import RichTextField

class EmailMessage(models.Model):
    subject = models.CharField(max_length=100)
    message = RichTextField()

    def __str__(self):
        return self.subject
    
class SignMessage(models.Model):
    subject = models.CharField(max_length=100)
    message = RichTextField()

    def __str__(self):
        return self.subject


# Create your models here.
class Click(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
      
class Recipient(models.Model):
    email = models.EmailField(unique=True)