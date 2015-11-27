from process.models import Activity,DailyStats
from django import forms
from getId.models import Id
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory


def validate_id(value):
	if not Id.objects.filter(userid=value).exists():
		raise ValidationError(u'Your id does not Exist')
	elif not User.objects.filter(username=value).exists():
		raise ValidationError(u'You are not registered')

class ProcessForm(forms.ModelForm):
    x = forms.CharField()
    y = forms.CharField()
    z = forms.CharField()
    flag = forms.BooleanField(required=False)
    userid = forms.CharField(validators = [validate_id], required=True)
    class Meta:
        model = Activity
        fields = ('userid', 'x', 'y', 'z', 'flag')

class DailyStatForm(forms.ModelForm):
    userid = forms.CharField(required=True)
    date = forms.CharField()
    walkingTime = forms.CharField()
    sittingTime = forms.CharField()
    suggestionCount = forms.CharField()
    class Meta:
        model = DailyStats
        fields = ('userid', 'date', 'walkingTime', 'sittingTime', 'suggestionCount')


