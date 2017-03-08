from django.contrib import admin

# Register your models here.

from .models import BasicInformation, Award, Transcript

admin.site.register(BasicInformation)

admin.site.register(Award)

admin.site.register(Transcript)
