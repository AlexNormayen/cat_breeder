#-*- coding: utf-8 -*-

from django import forms
from .models import Cat

class PictureForm(forms.Form):
    picture = forms.FileField(label='картинка')


class ParametrListForm(forms.Form):
    parametr_list = forms.CharField(label="новые", required=False)

class CatForm(forms.Form):
    breed       =    forms.CharField(label='Порода', max_length=256)
    name_cat    =    forms.CharField(label='Имя кота', max_length=16)
    age         =    forms.IntegerField(label='Возрвст', min_value=0)
    description =    forms.CharField(label= 'Описание', widget=forms.Textarea, required=False)
    parametr    =    forms.CharField(label= 'Характеристики', widget=forms.Textarea, required=False)
 


class CatModelForm(forms.ModelForm):
        
    #тут создается сама форма, если это надо
    
    class Meta:
        model = Cat
        fields = ['breed', 'name_cat', 'age', 'description']


    
 
