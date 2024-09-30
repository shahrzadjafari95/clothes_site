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
    products = All_Type_Clothes.objects.filter(status='available',
                                               gender__in=('male', 'sport'), published_date__lte=timezone.now())
    # Filter products by the category name passed in the URL
    if kwargs.get('cat_name') is not None:
        products = products.filter(category__name_category=kwargs['cat_name'])


def women(request):
    return render(request, 'women.html')
