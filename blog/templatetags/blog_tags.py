from django import template
from django.db.models import Count, Q
from django.utils import timezone
from blog.models import Post, Category, Comment

register = template.Library()


@register.inclusion_tag('blog/recent-post.html')
def latest_post(arg=3):
    posts = Post.objects.filter(status='A', published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/popular-post.html')
def popular_post(arg):
    posts = Post.objects.filter(status='A', published_date__lte=timezone.now()).order_by('-counted_view')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/categories.html')
def categories(status='A'):
    all_categories = Category.objects.annotate(post_count=Count('posts', filter=Q(posts__status=status) &
                                                                                Q(posts__published_date__lte=timezone.now()))).filter(
        post_count__gt=0).order_by('-post_count')  # Only show categories with posts
    return {'categories': all_categories}


@register.simple_tag(name='comment_count')
