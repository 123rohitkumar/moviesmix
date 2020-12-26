from django import forms
from .models import movie
from django.core import validators

class MovieForm(forms.ModelForm):
    class Meta:
        model = movie
        fields = ['rdate','moviename','hero','heroiene','rating']


    #Field level validation...       
    # def clean_hero(self,*args,**kwargs):
    #     hero = self.cleaned_data['hero']
    #     #hero = self.cleaned_data.get('hero')
    #     if len(hero)<4:
    #         raise forms.ValidationError("lenght of field should be greater then 4:")
    #     else:
    #         return hero

    #form level validations...
    def clean(self):
        print("Total form validations..")
        cleaned_data = super().clean()
        hero = cleaned_data['hero']
        if len(hero)<4:
            raise forms.ValidationError("lenght of field should be greater then 4:")
        

  

    

        

    
   
