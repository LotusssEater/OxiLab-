from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    user = request.user
    if user.has_perm('blog.admin'):
        posts = Post.objects.filter(
            published_date_lte=timezone.now()).orderby('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        return render(request, 'blog/Inicio.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    
    

