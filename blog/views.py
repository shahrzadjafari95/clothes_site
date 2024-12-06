from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import CommentForm, NewsletterForm
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

    # Handle search queries
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
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

    # Capture the full URL of the current page to use as the 'next' URL
    next_url = request.build_absolute_uri()

    if post.login_required:
        # If login is required and the user is not authenticated, redirect to the login page with the 'next' URL
        if not request.user.is_authenticated:
            return redirect(f'/accounts/login/?next={next_url}')

    # Continue processing for posts that don't require login or after login is successful
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Save the comment but don't commit to the database yet
            comment.post = post  # Set the post for the comment
            comment.save()  # Now save the comment to the database
            messages.success(request,
                             'Your comment has been posted successfully. After checking, it will be displayed '
                             'on the screen.')
        else:
            messages.error(request, 'There was an error with your comment.')

    comments = Comment.objects.filter(approved=True, post=post.id).order_by('-created_date')
    form = CommentForm()
    post.counted_view += 1
    post.save()

    contex = {
        'post': post,
        'form': form,
        'next': posts.filter(published_date__gt=post.published_date).order_by('published_date').first(),
        'previous': posts.filter(published_date__lt=post.published_date).order_by('-published_date').first(),
        'comments': comments
    }

    return render(request, 'blog/single-blog.html', contex)


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing to our newsletter!')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = NewsletterForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'form': form})  # redirect to referring page
