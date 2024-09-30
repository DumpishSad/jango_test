from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def games(request):
    return render(request, 'games.html')


def cart(request):
    return render(request, 'cart.html')
