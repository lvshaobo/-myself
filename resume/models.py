from django.db import models

# Create your models here.

class BasicInformation(models.Model):
    name = models.CharField(max_length=50)
    eduation = models.CharField(max_length=50)
    major = models.CharField(max_length=50)


class Award(models.Model):
    basic_information = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    time = models.DateField(verbose_name='time of award')

class Transcript(models.Model):
    basic_information = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    
    
