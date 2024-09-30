from django.shortcuts import render


def games_view(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'The Witcher 3']}
    return render(request, 'games.html', context)


def home_view(request):
    return render(request, 'home.html')


def cart_view(request):
    return render(request, 'cart.html')
