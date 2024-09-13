from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from FoodFinder.views import home_view  # Import the home view from your app
from FoodFinder.views import CustomLogoutView  # Import the custom logout view

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', home_view, name='home'),  # Home page view
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for authentication
    path('accounts/logout/', CustomLogoutView.as_view(), name='account_logout'),  # Custom logout view
]

# Optionally include debug toolbar routes during development
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
