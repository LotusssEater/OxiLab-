from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('Comunity/', views.Comunity, name='Comunity'),
    path('Discover/', views.Discover, name='Discover'),
    path('Login/', views.Login, name='Login'),
    path('Signup/', views.Signup, name='Signup'),
]
