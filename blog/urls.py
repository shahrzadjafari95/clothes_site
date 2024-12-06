from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [path('', views.blog_home,  name='blog-home'),
               path('post-<int:pid>', views.single_blog, name='single-blog'),
               path('category/<str:cat_name>/', views.blog_home, name='category'),
               path('tag/<str:tag_name>/', views.blog_home, name='tag'),
               path('author/<str:author>/', views.blog_home, name='author'),
               path('newsletter/', views.newsletter_view, name='newsletter'),

               ]
