from django.urls import path
from . import views

urlpatterns = [
    path('',views.allblogs, name='blogName'),
    path('<int:blog_id>/', views.detail, name='detail')
              ]

#   root is where you should look for info, and the path is MEDIA_URL
#   static is a whole app that allows to serve up images,files, etc...
