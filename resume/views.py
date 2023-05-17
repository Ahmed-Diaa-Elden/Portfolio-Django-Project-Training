from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import Contact
from .forms import ContactForm


# Create your views here.
def resume(request):
		today = datetime.datetime.now()
		return render(request, "resume.html", {"today": today})

def contactFormValidationList(request):
  # dictionary for initial data with
  # ﬁeld names as keys
  context ={}
  # add the dictionary during initialization
  context["dataset"] = Contact.objects.all()
  return render(request, "contactFormValidationList.html", context)

def contactFormValidation(request):
	if request.method =='POST':
		details = ContactForm(request.POST)
		if details.is_valid():
			contact = details.save(commit = False)
			contact.save()
			return redirect('contactFormValidationList')
		else:
			return render(request, "contactFormValidation.html", {'form':details})
	else:
		form = ContactForm(None)
		return render(request, 'contactFormValidation.html', {'form':form})
