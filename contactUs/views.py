from django.shortcuts import render
from contactUs.forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect


def contactUs(request):
	if request.method == 'POST':
	 	form= ContactForm(data=request.POST)
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    message = form.cleaned_data['message']
		    sender = form.cleaned_data['sender']
		    cc_myself = form.cleaned_data['cc_myself']

		    recipients = ['nfarve@mit.edu']
		    if cc_myself:
		        recipients.append(sender)

		    send_mail(subject, message, sender, recipients)
		    return HttpResponseRedirect('/contact#thanks')
	else:
		form = ContactForm()
		return render_to_response('contact.html', {'ContactForm': form}, context_instance=RequestContext(request))
