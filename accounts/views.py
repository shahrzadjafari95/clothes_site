from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
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

            if user:
                login(request, user)

                # Redirect to 'next' if provided, else to home
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('/')

    else:
        form = AuthenticationForm()

    # Render the login form and pass 'next' as context
    context = {
        'form': form,
        'next': next_url,  # Pass 'next' to the template
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    # - Use `HttpResponseRedirect(request.META.get('HTTP_REFERER'))` to redirect users back to the previous page after
    # a specific action (e.g., form submission, comment posting).
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def register(request):
    # Redirect authenticated users to the home page
    if request.user.is_authenticated:
        return redirect('/')

    # Capture 'next' from POST or GET request (form or URL)
    next_url = request.POST.get('next') or request.GET.get('next')

    if request.method == "POST":
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            user = form.save()

            # Authenticate the user after registration
            username_or_email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
