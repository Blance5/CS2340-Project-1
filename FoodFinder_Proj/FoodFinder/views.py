# home/views.py
from django.shortcuts import render
from allauth.account.views import EmailView
from allauth.account.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Restaurant
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


#def home_view(request):
#   return redirect(request, 'home.html')

@login_required
@csrf_exempt
def favorite_restaurant(request):
    if request.method == 'POST':
        restaurant_id = request.POST.get('restaurant_id')
        restaurant_name = request.POST.get('restaurant_name')
        restaurant_rating = request.POST.get('restaurant_rating')

        # Get the favorite restaurants list from the session, or initialize if not present
        favorite_restaurants = request.session.get('favorite_restaurants', [])

        # Check if the restaurant is already favorited
        existing_restaurant = next((r for r in favorite_restaurants if r['id'] == restaurant_id), None)

        if existing_restaurant:
            # If it's already favorited, remove it (unfavorite)
            favorite_restaurants = [r for r in favorite_restaurants if r['id'] != restaurant_id]
            status = 'unfavorited'
        else:
            # Otherwise, add it to favorites
            favorite_restaurants.append({
                'id': restaurant_id,
                'name': restaurant_name,
                'rating': restaurant_rating,
            })
            status = 'favorited'

        # Save the updated favorites list back to the session
        request.session['favorite_restaurants'] = favorite_restaurants
        request.session.modified = True  # Mark the session as modified

        return JsonResponse({'status': status})

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
            address = request.POST['address']
            newrestaurant = Restaurant.objects.create(place_id=place_id, name=name, rating=rating, address=address)
            newrestaurant.favorites.add(request.user)
    return render(request, 'home_logged_in.html')

@login_required
def profile_view(request):
    # Retrieve the favorite restaurants from the session
    favorite_restaurants = request.session.get('favorite_restaurants', [])

    return render(request, 'profile.html', {
        'user': request.user,
        'fav_restaurant': favorite_restaurants,
    })

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