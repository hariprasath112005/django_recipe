from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def chicken_biriyani(request):
    return render(request, 'chicken_biriyani.html')

@login_required
def rasam(request):
    return render(request, 'rasam.html')

@login_required
def sambar(request):
    return render(request, 'sambar.html')

@login_required
def chicken65(request):
    return render(request, 'chicken65.html')

@login_required
def prawn_fry(request):
    return render(request, 'prawn_fry.html')

@login_required
def fish_fry(request):
    return render(request, 'fish_fry.html')

@login_required
def kara_kolambu(request):
    return render(request, 'kara_kolambu.html')

@login_required
def potato_fry(request):
    return render(request, 'potato_fry.html')

@login_required
def meen_kolambu(request):
    return render(request, 'meen_kolambu.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
       
        if not User.objects.filter(username=username).exists():
    
            messages.error(request, 'Invalid Username')
            return redirect('/login')
         
      
        user = authenticate(username=username, password=password)
         
        if user is None:
            
            messages.error(request, "Invalid Password")
            return redirect('/login')
        else:
           
            login(request, user)
            return redirect('/')
     
    
    return render(request, 'login.html')
 

def register(request):
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            
            user = User.objects.filter(username=username)
            
            if user.exists():
            
                messages.info(request, "Username already taken!")
                return redirect('/register')
            
            
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username
            )
            
    
            user.set_password(password)
            user.save()
            
            
            messages.info(request, "Account created Successfully!")
            return redirect('/login')

    except ValueError:
        return render(request, 'register.html')

        
    return render(request, 'register.html')