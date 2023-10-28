from django.shortcuts import render

from .models import UserMessage

# Create your views here.
def usermessage(request):
    if request.method == "POST":
        username = request.POST['uemail']
        message = request.POST['umessage']

        new_message = UserMessage(username = username, message = message)
        new_message.save()

    return render(request, "usermessage.html")