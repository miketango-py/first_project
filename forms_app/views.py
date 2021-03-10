#form -- import

#for linking to the pages on 'templates' folder
from django.shortcuts import render#import render

#import the function 'contact_form' from 'forms.py'
from .forms import contact_form

#functions -- classes
def contacts(request):#start contacts

	#variables
	form = ""; context = ""#form and context for contact page

	#code
	form = contact_form()#assigning the contact message (with all the variables)
	context = {"form" : form}#assigning the form to the context (a dictionary)

	#the function returns an .html page
	return render (request, "contact.html", context)#returning the 'contact.html' page and the contact form

#end contacts

#code