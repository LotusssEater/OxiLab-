from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def Inicio(request):
    return render(request, 'blog/Inicio.html')  

def AboutUs(request):
    return render(request, 'blog/AboutUs.html')    
    
def Comunity(request):
    return render(request, 'blog/Comunity.html')      

def Discover(request):
    return render(request, 'blog/Discover.html') 

def Login(request):
    return render(request, 'blog/Login.html')     

def Signup(request):
    return render(request, 'blog/Signup.html')       