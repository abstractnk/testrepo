from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Dreamreal
from django.core.mail import send_mail
from myapp.forms import LoginForm


import datetime

def hello(request, name):
   text = "<h1>welcome to my app number Mr. %s!</h1>"% name
   return HttpResponse(text)
   
def time(request):
   today = datetime.datetime.now().date()
   return render(request, "myapp\hell.html", {"today" : today})
   

def crudops(request):
   #Creating an entry
   
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   
   #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   #Read a specific entry:
   sorex = Dreamreal.objects.get(name = "sorex")
   res += 'Printing One entry <br>'
   res += sorex.name
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()
   
   #Update
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   res += 'Updating entry<br>'
   
   dreamreal = Dreamreal.objects.get(name = 'sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()
   
   return HttpResponse(res)
   

def sendSimpleEmail(request,emailto):
   res = send_mail("hello Nanda", "Saukhyama?", "nandakishore01995@gmail.com", [emailto])
   return HttpResponse('%s'%res)

   
def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = Loginform()
		
   return render(request, 'myapp/loggedin.html', {"username" : username})