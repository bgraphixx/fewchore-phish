from django.shortcuts import HttpResponse, render
from .models import Click

def track_click(request):
    email = request.GET.get('email')
    if email:
        Click.objects.create(email=email)
        return HttpResponse("Thank you for clicking! You have been phished")
    return HttpResponse("Invalid request")


def clicks_list(request):
    clicks = Click.objects.all()
    return render(request, 'click_lists.html', {'clicks': clicks})