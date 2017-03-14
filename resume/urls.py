from django.conf.urls import url

from . import views

from .models import BasicInformation

app_name = 'resume'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^award$', views.AwardView.as_view(template_name="resume/award.html"), name='award'),
]
