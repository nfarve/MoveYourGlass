from django.db import models

# Create your models here.
class Activity(models.Model):
    userid = models.CharField(max_length=25)
    currentDate= models.DateField("last edited", auto_now = True)
    previousTotal = models.CharField(max_length=300000)
    currentTotal = models.CharField(max_length =10000)
    x = models.CharField(max_length=10000000)
    y = models.CharField(max_length=10000000)
    z = models.CharField(max_length=10000000)
    resultOn = models.CharField(max_length=10000000)
    
    def __unicode__(self):
    	return self.userid

