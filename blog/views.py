from django.shortcuts import render, get_object_or_404
from .models import Post
from markdown import markdown

# Create your views here.

def blog_index(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/blog_index.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    post.content = markdown(post.content, extensions=['fenced_code', 'codehilite'])
    return render(request, 'blog/blog_detail.html', {'post': post})