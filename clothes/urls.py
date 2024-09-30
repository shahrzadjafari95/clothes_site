from django.urls import path
from clothes import views


app_name = 'clothes'

urlpatterns = [path('', views.index,  name='home_page'),
               path('contact/', views.contact, name='contact'),
               path('men-clothes/', views.men, name='men-clothes'),
               path('women-clothes/', views.women, name='women-clothes'),
               path('women/<str:cat_name>', views.women, name='women_category'),
               path('men/<str:cat_name>/', views.men, name='men_category'),
]
