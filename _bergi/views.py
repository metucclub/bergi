from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("bergi's index")

# Create your views here.
