from django.conf.urls import url

from .views import *

app_name = 'resume'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^award$', award, name='award'),
]
