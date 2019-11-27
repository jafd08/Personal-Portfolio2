from django.db import models
import datetime
# Create your models here.



class Job(models.Model):  # this model.Model lest us create a class and save it on database
    image1 = models.ImageField(upload_to='img/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
