from registration.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from getId.models import Id
from django.core.exceptions import ValidationError

def validate_id(value):
	if not Id.objects.filter(userid=value).exists():
		raise ValidationError(u'Your id did not match')
	elif Id.objects.get(userid=value).usedFlag:
		raise ValidationError(u'This id has already been used')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password')

class UserProfileForm(forms.ModelForm):
    sex = forms.TypedChoiceField(coerce=lambda x: x=='True',choices=((True,'Male'), (False, 'Female')), widget = forms.RadioSelect)
    userid = forms.CharField(validators = [validate_id], required=True)
    class Meta:
        model = UserProfile
        fields = ('userid','sittingDaily', 'walkingDaily', 'sittingWeekly', 'walkingWeekly', 'ageGroup', 'sex', 
                    'workoutFreq', 'sittingTime','participant', 'sittingEstimate', 'walkingEstimate')


class UserRegisteredForm(forms.ModelForm):
	class Meta:
		model = User
		fields= ('username',)

