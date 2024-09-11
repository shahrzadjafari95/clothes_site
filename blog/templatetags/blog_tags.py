from django import template
from django.utils import timezone
from blog.models import Post, Category

register = template.Library()


@register.simple_tag
def count_view(pid):
    posts = Post.objects.filter(status='A', published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=pid)
    post.counted_view += 1
    post.save()
    return ''


@register.inclusion_tag('blog/recent-post.html')
def latest_post(arg=3):
    posts = Post.objects.filter(status='A', published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/popular-post.html')
def popular_post(arg):
    posts = Post.objects.filter(status='A', published_date__lte=timezone.now()).order_by('-counted_view')[:arg]
    return {'posts': posts}

