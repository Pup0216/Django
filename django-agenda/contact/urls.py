from django.urls import path
from . import views


app_name = 'contact'
urlpatterns = [
    path('<int:id>/', views.contact, name='contact'),
    path('', views.index, name='index'),
]
