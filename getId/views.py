from django.http import HttpResponse
from getId.models import Id
import random
import string

# Create your views here.
def index(request):
	generatedId = "A0O1P91CYE"
	while Id.objects.filter(userid=generatedId).exists():
		generatedId=name_generator()
	newid = Id(userid=generatedId)
	newid.save()
	return HttpResponse(generatedId)

def name_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))