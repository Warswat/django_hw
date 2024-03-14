from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_dict = {
        'id': 'id',
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    sorting = request.GET.get('sort', 'id')
    template = 'catalog.html'
    context = {'phones':Phone.objects.all().order_by(sort_dict[sorting]).values()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print(Phone.objects.get(slug = slug))
    context = {'phone' : Phone.objects.get(slug = slug)}
    return render(request, template, context)
