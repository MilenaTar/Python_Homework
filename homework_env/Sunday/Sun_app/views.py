from django.shortcuts import render
from django.http import HttpResponse
from .models import Film



def film (request):
    films = Film.objects.all()
    data = {'film': films}
    return render(request, "Sun_app/Sun_app.html", data)


