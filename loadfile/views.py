from .forms import UploadFileForm
from .models import UploadFileModel
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView


class UploadFile(FormView):
	def get(self, request):
		upload = UploadFileForm
		return render(request, 'loadfile/loadfile.html', {'upload':upload})

	def post(self, request):
		form_class  = UploadFileForm
		form = self.get_form(form_class)
		name = request.POST.get('title')
		files = request.FILES.getlist('file')		
		if form.is_valid():	
			for f in files:
				instance = UploadFileModel(title=name, file = f)
				instance.save()		
			return redirect('/loadfile/')			
						
		