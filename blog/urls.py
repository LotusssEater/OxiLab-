from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('Inicio/', views.Inicio, name='Inicio'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('Comunity/', views.Comunity, name='Comunity'),
    path('Discover/', views.Discover, name='Discover'),
    path('Login/', views.Login, name='Login'),
    path('Signup/', views.Signup, name='Signup'),
]
