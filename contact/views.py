from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Form
from .models import contactForm
from django.views import View
# Create your views here.
class contact(View):
	def get(self, request):
		contact_F = contact_Form
		return render(request, 'contact/contact.html', {'contact_F': contact_F})

	def post(self, request):
		if request.method == "POST":
			contact_F = contact_Form(request.POST)
			if contact_F.is_valid():
				save_contact_F = contactForm( username = contact_F.cleaned_data['username'],
					email = contact_F.cleaned_data['email'],
					body = contact_F.cleaned_data['body'])
				save_contact_F.save()
				return HttpResponse('save ok')
