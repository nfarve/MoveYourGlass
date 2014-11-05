from django.conf.urls import patterns, url

from landing import views

urlpatterns = patterns('', 
    url(r'^$', views.home, name ='home')

)