from django.urls import path
from . import views


app_name = 'contact'
urlpatterns = [

    path('search/',views.search,name='search'),
    path('', views.index, name='index'),

    #contacts
    path('contact/<int:id>/', views.contact, name='contact'),
    path('contact/create/',views.create, name='create'),
    path('contact/<int:id>/update',views.contact, name='contact')

]
