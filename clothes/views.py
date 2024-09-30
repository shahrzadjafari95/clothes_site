from django.contrib import messages
from django.shortcuts import render
from clothes.forms import ContactForm
from clothes.models import All_Type_Clothes, Category


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


def men(request, **kwargs):
    all_categories = Category.objects.all()
    products = All_Type_Clothes.objects.filter(status='available',
                                               gender__in=('male', 'sport'), published_date__lte=timezone.now())
    # Filter products by the category name passed in the URL
    if kwargs.get('cat_name') is not None:
        products = products.filter(category__name_category=kwargs['cat_name'])
    products = Paginator(products, 9)  # Show 9 products per page
    try:
        # Get the page number from the request's GET parameters
        page_number = request.GET.get('page')
        products = products.get_page(page_number)
    except PageNotAnInteger:  # if user enter a string or not int object
        products = products.get_page(1)  # return page1
    except EmptyPage:
        products = products.get_page(1)
    context = {'products': products, 'categories': all_categories}
    return render(request, 'men.html', context)


    return render(request, 'women.html')
def women(request, **kwargs):
