from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name=''),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('geolocate/', views.geolocate, name='geolocate'),
    path('locateme/', views.locateme, name='locateme'),
    path('home/', views.homepage, name='home'),

]
