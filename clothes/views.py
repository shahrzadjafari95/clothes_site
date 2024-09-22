from django.shortcuts import render
from clothes.forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully')


def men(request):
    return render(request, 'men.html')


def women(request):
    return render(request, 'women.html')