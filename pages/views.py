from django.shortcuts import render
from .models import Teams
from cars.models import Car

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    featured_cars = Car.objects.order_by('created_at').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_at')
    context = {
        'teams': teams,
        "featured_cars": featured_cars,
        "all_cars": all_cars,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    teams = Teams.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')