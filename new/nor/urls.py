from django.urls import path
# from .views import home erku tarberakn el ok 
from . import views
urlpatterns = [
    path ("", views.home, name = "home_page"),
    path("about", views.about, name = 'about_us'),
]