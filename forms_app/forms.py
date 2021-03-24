from django import forms
from .models import Contatto

class FormContatto(forms.ModelForm): 
    class Meta: 
        model=Contatto
        fields="__all__"
        widgets = {
            'name' : forms.TextInput(attrs = {'placeholder':'Fill this field', 'class':'form-control'}),
            'surname' : forms.TextInput(attrs = {'placeholder':'Fill this field', 'class':'form-control'}),
            'email' : forms.EmailInput(attrs = {'placeholder':'Fill this field', 'class':'form-control'}),
            'context' : forms.Textarea(attrs = {'placeholder':'Write', 'class':'form-control'})
        }

