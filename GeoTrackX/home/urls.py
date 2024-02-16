from django.urls import path
from . import views
from .views import submit_contact, admin_view

urlpatterns = [
    path('', views.homepage, name=''),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('geolocate/', views.geolocate, name='geolocate'),
    path('locateme/', views.locateme, name='locateme'),
    path('home/', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('submit_contact/', submit_contact, name='submit_contact'),
    path('admin_view/<int:form_id>/', admin_view, name='admin_view'),
    # path('user/', views.user, name='user'),

]
