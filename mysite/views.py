#from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup


def home(request):
  search=request.POST.get('search')
  #print(search)
  stuff_for_frontend ={
    'search':search,
  }
  return render(request , 'base.html', stuff_for_frontend)

def coaching(request):
  return render(request , 'main/coaching.html')

def contact(request):
  return render(request , 'main/contact.html')
