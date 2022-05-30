from django.shortcuts import render
from django.http import HttpResponse

from .models import Person
# Create your views here.

def index(request):
    return render(request, "login/index.html")

def person(request, person_id):
    profile_name = Person.objects.get(pk = person_id)
    return HttpResponse("Hello, world. You're at the login page of {}.".format(profile_name))
