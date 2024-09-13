# home/views.py
from django.shortcuts import render
from allauth.account.views import EmailView
from allauth.account.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect

def home_view(request):
    return render(request, 'home.html')


class CustomEmailView(EmailView):
    template_name = 'allauth/account/email.html'

class CustomLogoutView(TemplateView):
    template_name = 'account/logout.html'

    #3def get(self, request, *args, **kwargs):
      #3  logout(request)
        #return redirect('home')  # Redirect to home page after logout