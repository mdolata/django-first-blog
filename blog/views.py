from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .simple_logger import logger


def post_list(request):
    logger(request, 'post_list')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def home(request):
    logger(request, 'home')
    return render(request, 'blog/home.html', {})


def post_detail(request, pk):
    logger(request, 'post_detail_1')
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
