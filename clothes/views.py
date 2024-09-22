from django.shortcuts import render
from clothes.forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')
    if request.method == 'POST':
        form = ContactForm(request.POST)


def men(request):
    return render(request, 'men.html')


def women(request):
    return render(request, 'women.html')