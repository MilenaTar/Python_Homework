
from django.urls import path
from . import views


urlpatterns = [
    path('', views.greeting, name = "Greeting"),
    path('introduction', views.introduction, name = "Introduction"),
    path('clock', views.clock, name = "Clock"),
    path('dict_', views.dict_, name = "dict_"),

]
