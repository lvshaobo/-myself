from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import BasicInformation

"""
def index(request):
    return HttpResponse('Hello, Everyone. Welcome to my resume.')
"""

def index(request):
    return render(request, 'resume/index.html', context={'resume_list': BasicInformation.objects.all()})
