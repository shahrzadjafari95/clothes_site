from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [path('', views.blog_home,  name='blog-home'),
               path('post-<int:pid>', views.single_blog, name='single-blog'),

]
