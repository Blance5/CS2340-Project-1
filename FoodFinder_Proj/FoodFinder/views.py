# home/views.py
from django.shortcuts import render
from allauth.account.views import EmailView
from allauth.account.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Restaurant


#def home_view(request):
#   return redirect(request, 'home.html')


# View for logged in users
@login_required  # Ensures only logged in users can access this view
def home_logged_in(request):
    if request.method == 'POST':
        place_id = request.POST['place_id']

        # Check if the restaurant already exists
        if Restaurant.objects.filter(place_id=place_id).exists():
            restaurant = Restaurant.objects.get(place_id=place_id)
            if restaurant.favorites.filter(id=request.user.id).exists():
                restaurant.favorites.remove(request.user)
            else:
                restaurant.favorites.add(request.user)
        else:
            name = request.POST['name']
            rating = request.POST['rating']
            newrestaurant = Restaurant.objects.create(place_id=place_id, name=name, rating=rating)
            newrestaurant.favorites.add(request.user)
    return render(request, 'home_logged_in.html')

@login_required
def profile_view(request):
    fav_restaurant = Restaurant.objects.filter(favorites=request.user)
    context = {
        'fav_restaurant': fav_restaurant,
        'user': request.user
    }
    return render(request, 'profile.html', context)

# View for logged out users
def home_logged_out(request):
    return render(request, 'home_logged_out.html')

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('home_logged_in')  # URL name for the logged-in view
    else:
        return redirect('home_logged_out')  # URL name for the logged-out view


class CustomEmailView(EmailView):
    template_name = 'allauth/account/email.html'


class CustomLogoutView(TemplateView):
    template_name = 'account/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home_redirect')  # Redirect to home page after logout