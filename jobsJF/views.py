from django.shortcuts import render
from .models import Job

# Create your views here.

def home(request):
    jobsObjs = Job.objects
    print('jobsObjs: ', jobsObjs)
    return render(request, 'jobsJF/home.html' , {'jobs': jobsObjs})
