from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import static
from django.contrib.auth.decorators import user_passes_test

def Homepage(request):
	return render(request, 'main/home.html')

def Aboutpage(request):
	return render(request, 'main/about.html')

def Portfolio(request):
	return render(request, 'main/portfolio.html')

def Register(request):
	if request.method == 'POST' :
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')

		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.email = email
		newuser.set_password(password)
		newuser.save()
		return redirect('home-page')
	return render(request, 'main/register.html')
	