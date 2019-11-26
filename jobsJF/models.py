from django.db import models
import datetime
# Create your models here.

datenow = datetime.datetime.now()

class Job(models.Model):  # this model.Model lest us create a class and save it on database
    image1 = models.ImageField(upload_to='img/')
    summary = models.CharField(max_length=200)


