"""Advertiser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        path('', views.HomePage, name= 'homepage'),
        path('login/', views.LoginIN, name = "login"),
        path('signup/', views.SignUP, name = "signup"),
        path('signup_user/', views.SignUP_User, name = "signup_user"),
        path('profile/', views.Profile, name = "profile"),
        path("logout/", views.LogOUT, name = "logout"),
        path("public/<pk>/", views.public_profile, name = "public_profile"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

