from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post


# Create your views here.
def blog_home(request):
    posts = Post.objects.filter(status='A', published_date__lte=timezone.now()).order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_blog(request, pid):
    posts = Post.objects.filter(status='A', published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=pid)
