from django.contrib import admin
from .models import Click, EmailMessage, Recipient, SignMessage
# Register your models here.
@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp')

@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message')

@admin.register(SignMessage)
class SignMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message')

@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('email',)