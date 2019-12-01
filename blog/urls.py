from django.conf.urls import url
from django.urls import path
from . import views as myviews
from django.contrib.auth import views as views_auth
from django.conf.urls import url, include
from rest_framework import routers
from blog.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('Inicio/', myviews.Inicio, name='Inicio'),
    path('', myviews.post_list, name='post_list'),
    path('post/new', myviews.post_new, name='post_new'),
    path('post/<int:pk>/edit/', myviews.post_edit, name='post_edit'),
    path('post/<int:pk>/', myviews.post_detail, name='post_detail'),
    path('post/<pk>/remove/', myviews.post_remove, name='post_remove'),
    path('AboutUs/', myviews.AboutUs, name='AboutUs'),
    path('Comunity/', myviews.Comunity, name='Comunity'),
    path('Discover/', myviews.Discover, name='Discover'),
    path('Login/', views_auth.LoginView.as_view(template_name='blog/Login.html'), name='Login'),
    path('Perfil/', myviews.Signup, name='Perfil'),
    path('Logout/', views_auth.LogoutView.as_view(next_page='Inicio'), name='Logout'),
    path('Signup/', myviews.Signup, name='Signup'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
