from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'), # koi bhi agr aata h path ya blank path lekr aata h to usko views k index func p bhej do or iss path ka naam rkhdo home
    path("about", views.about, name='About us'),  # on chrome :- http://127.0.0.1:8000/about
    path("services", views.services, name='Services'),
    path("contact", views.contact, name='Contact us'),
]