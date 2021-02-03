from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def home(requests):
	return HttpResponse("Hello world from Django!!!")


def about(requests):
	a = []
	for i in "hello":
		a.append(i)
	# return HttpResponse("<h1>This is about us.<br>{}</h1>".format(a))
	# return redirect

