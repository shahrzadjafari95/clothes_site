from django.urls import path
from accounts import views
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),  # login url
    path('logout/', views.logout_view, name='logout'),  # logout url
    path('register/', views.register, name='register'),  # signup(register) url
    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password-reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

