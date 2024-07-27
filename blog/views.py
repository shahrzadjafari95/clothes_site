from django.shortcuts import render


# Create your views here.
def blog_home(request):
    return render(request, 'blog/blog.html')


def single_blog(reqest):
    return render(reqest, 'blog/single-blog.html')
