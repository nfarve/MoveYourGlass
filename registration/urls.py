from django.conf.urls import patterns, url
from registration import views

urlpatterns = patterns('', 
    url(r'^$', views.register, name ='register'),
    url(r'^(?P<user_id>[\w\-]+)',views.checkIfRegistered, name='checkIfRegistered'),
   	
)