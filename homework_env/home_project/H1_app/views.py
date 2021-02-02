from django.shortcuts import render
from django.http import HttpResponse
import datetime


def greeting(requests):
	return HttpResponse("<h1 style= 'background-color:DodgerBlue';'> Sending you hello from my stuggling to understand this. </h1>")

def introduction(requests):
	return HttpResponse("<h2> This is my young project called Home.<img src='https://files.realpython.com/media/python-basics-wide2.f73a9e9bf9b8.jpg' alt='Python'style='width:500px;height:400px;'> </h2>")

def clock(requests):
	return HttpResponse("Date and time {}".format(datetime.datetime.now()))

def dict_(requests):
	dict1 ={}
	for i in range(1,16):
		dict1[i] = i**2
	return HttpResponse("{}".format(dict1))