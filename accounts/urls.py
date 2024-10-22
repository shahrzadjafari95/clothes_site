from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),  # login url
    path('logout/', views.logout_view, name='logout'),  # logout url
    path('register/', views.register, name='register'),  # signup(register) url
