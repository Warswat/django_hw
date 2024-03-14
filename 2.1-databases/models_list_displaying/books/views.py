from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {'books':Book.objects.all()}
    return render(request, template, context)


def books_date_view(request, pub_date):
    paginator = Paginator(Book.objects.all(),1)
    page = paginator.get_page(Book.objects.get(pub_date=pub_date).id)
    print(page)
    template = 'books/books_list.html'
    next = None
    prev = None
    if page.has_next():
        next = str(paginator.get_page(page.next_page_number())[0].pub_date)
        print(next)
    if page.has_previous():
        prev = str(paginator.get_page(page.previous_page_number())[0].pub_date)
        print(prev)
    context = {'books': page,
               'page': page,
               'next': next,
               'prev': prev,
               }
    return render(request, template, context)
