from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    
    # return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})

def styled_index(request):
    # return the rendered template
    return render(request, 'blog/styled-index.html', {})

def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    
    # return the rendered template
    return render(request, 'blog/post.html', {'post': post})
