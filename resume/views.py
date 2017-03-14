# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.views import generic

from django.http import HttpResponse

from .models import BasicInformation

class IndexView(generic.ListView):
    model = BasicInformation
    template_name = "resume/index.html"
    context_object_name = "basic_information_list"



def index(request):
    return render(request, 'resume/index.html',
        context={'basic_information': BasicInformation.objects.all()}
    )

def award(request):
    return render(request, 'resume/award.html',
        context={'basic_list': BasicInformation.objects.all()}
    )
