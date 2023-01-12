from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class registerUser(View):
	def get(self, request):
		register_Form = registerForm
		return render(request, 'usermember/register.html', {'register_Form':register_Form})
	def post(self, request):
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.create_user(username, email, password)
		user.save()
		return HttpResponse('save ok')



class loginUser(View):
	def get(self, request):
		login_Form = loginForm
		return render(request, 'usermember/login.html', {'login_Form':login_Form})
	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		try:
			user = authenticate(request, username=User.objects.get(email = username), password=password)
		except:
			user = authenticate(request, username=username, password=password)
		if user is not None:
			#return HttpResponse('login ok')
			login(request, user)
			return render(request,'usermember/private.html')

		else:
			return HttpResponse('login fail')

def logoutUser(request):
	logout(request)
	return redirect('usermember:login')


class privatePage(LoginRequiredMixin, View):
	login_url='/usermember/'
	def get(self, request):
		return render(request,'usermember/private.html')
