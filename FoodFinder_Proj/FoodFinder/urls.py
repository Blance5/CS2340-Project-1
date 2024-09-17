"""
URL configuration for FoodFinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomLogoutView, CustomEmailView, home_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home_view, name='home'),  # Home page view
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for authentication
    path('logout/', LogoutView.as_view(), name='logout'),  # Custom logout view
    path('email/', CustomEmailView.as_view(), name='account_email'),  # Custom email view
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns