from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),  # login url
