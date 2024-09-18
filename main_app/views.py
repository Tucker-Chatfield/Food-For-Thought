from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Restaurant
from .forms import ReviewForm
import requests

MY_API_KEY = 'Gg65rpmjeX_dtHi23G6_dX9GrUnRI8i-p5x4SSTcmyUi8C2pElUS-bvsn2nbuIrPc1QvfxV9lMxvGeVGmkeI3D8b8tIw7CfTqdvr36sXpCtPSIjMO493ccuH5QHqZnYx'

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

# def restaurant_index(request):
#     restaurants = Restaurant.objects.all()
#     return render(request, 'restaurants/index.html', {'restaurants': restaurants})

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    review_form = ReviewForm()
    return render(request, 'restaurants/detail.html', {'restaurant': restaurant, 'review_form': review_form})

def restaurant_index(request):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'bearer %s' % MY_API_KEY}
    params = {
        'location': 'San Francisco',
        'term': 'restaurants',
        'limit': 10
    }

    response = requests.get(url, headers=headers, params=params)
    restaurants = response.json().get('businesses', [])

    return render(request, 'restaurants/index.html', {'restaurants': restaurants})

def add_review(request, restaurant_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.restaurant_id = restaurant_id
        new_review.save()
    return redirect('restaurant-detail', restaurant_id=restaurant_id)