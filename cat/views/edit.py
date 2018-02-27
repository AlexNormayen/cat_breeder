 
from django.shortcuts import render, get_object_or_404

from restful import restful
from ..models import Cat
from ..forms import CatModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse


import sys

@restful
def edit(request, cat):
    
      
    
    if request.method == 'POST':
        raw_data = dict()
        raw_data.update( request.POST )
        
    
        
    tovar = get_object_or_404(Cat, pk=id_cat) 
    form = CatModelForm(instance=cat)
    
   
    return render(request, 'cat/cat_edit.html', locals())

@edit.method('POST')
def edit(request, id_cat):
     
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('cat:index'))
    if not request.user.user.is_superuser:
        if not request.user.has_perm('cat.change_cat'):
            return HttpResponseRedirect(reverse('cat:index'))
        
    raw_data = dict()
    raw_data.update( request.POST )
        
    cat = get_object_or_404(Cat, pk=id_cat) 
        
    form = CatModelForm(request.POST, instance=cat)
    if form.is_valid():
        form.save()   
        return render(request, 'cat/cat_edit.html', locals())
    else:
        return render(request, 'cat/cat_edit.html', locals())
