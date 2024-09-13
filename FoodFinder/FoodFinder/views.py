# home/views.py
from django.shortcuts import render
from allauth.account.views import EmailView
from allauth.account.views import LogoutView

def home_view(request):
    return render(request, 'home.html')


class CustomEmailView(EmailView):
    template_name = 'allauth/account/email.html'

class CustomLogoutView(LogoutView):
    template_name = 'allauth/account/logout.html'