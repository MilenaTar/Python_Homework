from django.shortcuts import render, redirect
from django.http import HttpResponse
import json


def greeting(request):
	context = {"":""}
	return  render(request, "Friends/Friends.html", context)

def actors(request):
	with open ("actors.json","r") as file:
		data = json.load(file)
	# data = {"new":[2,3,4,444,6],3:4,5:6}
	return render(request,"Friends/Friends2.html",data)

