from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def search_form(request):
    return render(request, 'books\search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        message = 'You search for: %r ' % request.GET['q']
        books = Book.object.filter(title_icontains=q)
        return render(request, 'search_result.html', {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term')
