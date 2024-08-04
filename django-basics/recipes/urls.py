from django.http import HttpResponse,HttpRequest
from recipes.views import home,about,contact
from django.urls import path



urlpatterns = [
    path('',home),
    path('about/',about),
    path('contact/',contact),
]