# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import BasicInformation

class IndexView(generic.ListView):
    model = BasicInformation
    template_name = "resume/index.html"
    context_object_name = "basic_information_list"


def index(request):
    return render(request, 'resume/index.html',
        context={'basic_information_list': BasicInformation.objects.all()}
    )


class AwardView(generic.ListView):
    model = BasicInformation
    context_object_name = "basic_information_list"


def award(request):
    return render(request, 'resume/award.html',
        context={'basic_information_list': BasicInformation.objects.all()}
    )


class IndexTemplateView(generic.TemplateView):
    template_name = "resume/index-template-view.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['basic_information_list'] = BasicInformation.objects.all()
        return context
