from django.contrib import messages
from django.shortcuts import render
from clothes.forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, "Your ticket didn't submit ")
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


    return render(request, 'men.html')
def men(request, **kwargs):
    all_categories = Category.objects.all()


def women(request):
    return render(request, 'women.html')
