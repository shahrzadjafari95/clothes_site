from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import CommentForm
from .models import Post, Comment


# Create your views here.
def blog_home(request, **kwargs):
    posts = Post.objects.filter(status='A', published_date__lte=timezone.now()).order_by('-published_date')
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author') is not None:
        posts = posts.filter(author__username=kwargs['author'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tag__name=kwargs['tag_name'])
    posts = Paginator(posts, 3)  # posts that filter by above conditions
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:  # if user enter a string or not int object
        posts = posts.get_page(1)  # return page1
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_blog(request, pid):
    posts = Post.objects.filter(status='A', published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=pid)
    comments = Comment.objects.filter(approved=True, post=post.id)
    if request.method == "POST":
        form = CommentForm(request.POST)
    post.counted_view += 1
    post.save()
    contex = {'post': post,
              # filter posts according published_date that great than current post published_date
              'next': posts.filter(published_date__gt=post.published_date).order_by('published_date').first(),
              'previous': posts.filter(published_date__lt=post.published_date).order_by('-published_date').first()}

    return render(request, 'blog/single-blog.html', contex)
