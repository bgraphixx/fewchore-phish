from django.contrib import admin
from .models import Click
# Register your models here.
@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp')