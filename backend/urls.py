"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('chicken_biriyani/', views.chicken_biriyani, name="chicken_biriyani"),
    path('rasam/', views.rasam, name="rasam"),
    path('sambar/', views.sambar, name="sambar"),
    path('fish_fry/', views.fish_fry, name="fish_fry"),
    path('potato_fry/', views.potato_fry, name="potato_fry"),
    path('prawn_fry/', views.prawn_fry, name="prawn_fry"),
    path('chicken65/', views.chicken65, name="chicken65"),
    path('kara_kolambu/', views.kara_kolambu, name="kara_kolambu"),
    path('meen_kolambu/', views.meen_kolambu, name="meen_kolambu"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register, name="register"),
]
