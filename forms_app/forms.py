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
            'nome' : forms.TextInput(attrs = {'placeholder':'Fill this field', 'class':'form-control'}),
            'cognome' : forms.TextInput(attrs = {'placeholder':'Fill this field', 'class':'form-control'}),
            'email' : forms.EmailInput(attrs = {'placeholder':'Fill this field', 'class':'form-control'}),
            'contenuto' : forms.Textarea(attrs = {'placeholder':'Write minimum 20 characters', 'class':'form-control'})
        }
    #end class Meta

    def clean_contenuto(self): #start clean_context; general sintax = clean_field_to_validate
        
        #code
        dati = self.cleaned_data["contenuto"]
        
        #"parola" is not admitted
        if "parola" in dati:#start if; error 1
            raise ValidationError ("The context is violating the site norms!")
        #end if

        #data too short
        if len(dati) < 20:#start if
            raise ValidationError("The context is too short!")
        #end if

        return dati

    #end clean_context
#end class FormContatto