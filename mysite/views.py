#from django.http import HttpResponse
from django.shortcuts import render
#from django.utils import timezone
import os
from twilio.rest import Client
from . import models
#from bs4 import BeautifulSoup

account_sid=os.getenv("ACCOUNT_SID")
token=os.getenv("TOKEN")
my_cell=os.getenv("MY_CELL")
my_twiliocell=os.getenv("MY_TWILIOCELL")

def peopleList(request):
  person=[request.POST.get('name'),request.POST.get('email'),request.POST.get('phone'),request.POST.get('msg')]
  return person

      
def home(request):
  return render(request , 'main/home.html')


def coaching(request):
  return render(request , 'main/coaching.html')

def aboutme(request):
  return render(request , 'main/about-me.html')

def massages(request):
  return render(request , 'main/massages.html')

def contact(request):
  newclient=peopleList(request)
  #smsToSend="Hi"
  print(newclient)   
  #sendSMS(smsToSend)
  return render(request , 'main/contact.html')

def info(request):
  info=request.POST.get('info')
  print(info)
  return render(request , 'main/info.html')

def sendSMS(msg):
  try:
    print(account_sid)
    print(token)
    client=  Client(account_sid, token)
    client.messages.create(to= my_cell , from_= my_twiliocell , body=msg)
    print("SMS sent")
  except:
    print("SMS didn't sent")









  

