from django.db import models

# Create your models here.
class Id(models.Model):
	date = models.DateField(auto_now= True)
	userid = models.CharField(max_length = 25, unique=True)
	usedFlag = models.BooleanField(default = False)

	def __unicode__(self):
		return self.userid