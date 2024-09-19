from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def chicken_biriyani(request):
    return render(request, 'chicken_biriyani.html')

def rasam(request):
    return render(request, 'rasam.html')


def sambar(request):
    return render(request, 'sambar.html')

def chicken65(request):
    return render(request, 'chicken65.html')

def prawn_fry(request):
    return render(request, 'prawn_fry.html')

def fish_fry(request):
    return render(request, 'fish_fry.html')

def kara_kolambu(request):
    return render(request, 'kara_kolambu.html')

def potato_fry(request):
    return render(request, 'potato_fry.html')


def meen_kolambu(request):
    return render(request, 'meen_kolambu.html')


def login_page(request):
    return render(request, 'login.html')