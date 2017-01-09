from django.shortcuts import render
from django.http import HttpResponse


def search_form(request):
    return render(request, 'books\search_form.html')


def search(request):
    if 'q' in request:
        message = 'You search for: %r ' % request.GET['q']
    else:
        message = 'You submitted a empty form.'
    return HttpResponse(message)
