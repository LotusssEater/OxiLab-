from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    return render(request, 'blog/Inicio.html', {})

