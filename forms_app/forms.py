#from -- import
from django import forms
#functions -- classes

#creating the class for the contact form
class contact_form (forms.Form):#start contact_form

	#variables
	name = ""; surname = ""#name and surname of the contact
	email = ""; content = ""#e-mail and content of the contact

	#code
	name = forms.CharField()#assigning name of the contact
	surname = forms.CharField()#assigning surname of the contact
	e_mail = forms.EmailField()#assigning e-mail of the contact
	
	#creating the textual area where the contact will put the message
	content = forms.CharField(widget = forms.Textarea (attrs = {"placeholder" : "Textual Area! You can write!"}))#assigning message of the contact

#end contact_form
#code