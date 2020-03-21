#from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import Client
#from bs4 import BeautifulSoup


def peopleList(request):
  person=[request.POST.get('name'),request.POST.get('email'),request.POST.get('phone')]
  return person

def home(request):
  print(peopleList(request))
  return render(request , 'main/home.html')


def coaching(request):
  return render(request , 'main/coaching.html')

def contact(request):
  print(peopleList(request))
  return render(request , 'main/contact.html')

def info(request):
  info=request.POST.get('info')
  print(info)
  return render(request , 'main/info.html')





  

