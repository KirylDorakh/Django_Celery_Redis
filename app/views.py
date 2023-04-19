from django.shortcuts import render

from .task import text


def index(request):
    text.delay()
    return render(request, 'index.html')
