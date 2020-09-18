from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html', {})


def privacy(request):
    return render(request, 'base/privacidade.html')
