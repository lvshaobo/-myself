from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

"""
def index(request):
    return HttpResponse('Hello, Everyone. Welcome to my resume.')
"""

def index(request):
    return render(request, 'resume/index.html') 
