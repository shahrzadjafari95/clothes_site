from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.


def login_view(request):
    # Redirect authenticated users to the home page
    if request.user.is_authenticated:
        return redirect('/')

    # Capture the 'next' URL from GET or POST
    next_url = request.POST.get('next') or request.GET.get('next') or '/'

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

