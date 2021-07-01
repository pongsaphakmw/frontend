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