from .task import text
from django.shortcuts import render




def index(request):
    text.delay()
    return render(request, 'index.html')
