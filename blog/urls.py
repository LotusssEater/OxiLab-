from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('Inicio/', views.Inicio, name='Inicio'),
    path('', views.post_list, name='post_list'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('Comunity/', views.Comunity, name='Comunity'),
    path('Discover/', views.Discover, name='Discover'),
    path('Login/', views.Login, name='Login'),
    path('Signup/', views.Signup, name='Signup'),
]
