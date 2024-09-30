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
from django.contrib.auth.views import LogoutView
from . import views
from .views import CustomLogoutView, profile_view


urlpatterns = [
    path('', views.home_redirect, name='home_redirect'),  # Home page view
    path('home_logged_in/', views.home_logged_in, name='home_logged_in'),
    path('home_logged_out/', views.home_logged_out, name='home_logged_out'),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for authentication
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Custom logout view
    path('accounts/email/', views.CustomEmailView.as_view(), name='account_email'),  # Custom email view
    path('profile/', profile_view, name='profile'),  # Add the profile URL here
    path('favorite/', views.favorite_restaurant, name='favorite_restaurant'),

    #[Issues] path('add_favorite/<int:place_id>/', views.add_favorite, name='add_favorite'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns