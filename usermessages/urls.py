from django.urls import path

from . import views


urlpatterns = [
    path("", views.usermessage, name="usermessage"),
]