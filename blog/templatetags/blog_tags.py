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
