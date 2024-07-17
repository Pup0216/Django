from django.urls import path
from . import views


app_name = 'contact'
urlpatterns = [

    path('search/',views.search,name='search'),
    path('', views.index, name='index'),

    #contacts
    path('contact/<int:id>/', views.contact, name='contact'),
    path('contact/create/',views.create, name='create'),
    path('contact/<int:contact_id>/delete', views.delete, name='delete'),
    path('contact/<int:contact_id>/update/',views.update, name='update'),
    #user
    path("user/create", views.register, name="register"),
    path('user/login',views.userLogin,name='login'),
    path('user/logout',views.userLogout,name='logout'),
    path('user/update',views.userUpdate,name='user_update'),


]
