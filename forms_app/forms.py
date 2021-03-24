#from -- import
from django import forms
from django.core.exceptions import ValidationError
from .models import Contatto

#functions -- class
class FormContatto(forms.ModelForm): #start class FormContatto
    class Meta: 
        model=Contatto
        fields="__all__"
        widgets = {
            'name' : forms.TextInput(attrs = {'placeholder':'Fill this field', 'class':'form-control'}),
            'surname' : forms.TextInput(attrs = {'placeholder':'Fill this field', 'class':'form-control'}),
            'email' : forms.EmailInput(attrs = {'placeholder':'Fill this field', 'class':'form-control'}),
            'context' : forms.Textarea(attrs = {'placeholder':'Write minimum 20 characters', 'class':'form-control'})
        }
#end class FormContatto

def clean_context(self): #start clean_context; general sintax = clean_field_to_validate
    
    #code
    data = self.cleaned_data["context"]
    
    #"parola" is not admitted
    if "parola" in data:#start if; error 1
        raise ValidationError ("The context is violating the site norms!")
    #end if

    #data too short
    if len(data) < 20:#start if
        raise ValidationError("The context is too short!")
    #end if

    return data

#end clean_context