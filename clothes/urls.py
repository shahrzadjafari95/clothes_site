from django.urls import path
from clothes import views


app_name = 'clothes'

urlpatterns = [path('', views.index,  name='home_page'),
               path('contact/', views.contact, name='contact'),


]
