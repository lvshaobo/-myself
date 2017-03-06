from django.db import models

# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    birthday = models.DateTimeField('time of birth')
