from django.conf.urls import patterns, url

from process import views

urlpatterns = patterns('', 
    url(r'^$', views.process, name ='process')

)