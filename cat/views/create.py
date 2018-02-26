#!/usr/bi/env pethon3
#-*- coding: utf-8 -*-

from  django.shortcuts  import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..forms import CatModelForm

from ..models import Cat

from restful import restful


@restful
def create(request):
    
    cat = Cat()
    form = CatModelForm(instance=cat)
    
    return render(request, 'cat/cat_edit.html', locals())

@create.method('POST')
def create(request):
    cat = Cat()
    form = CatModelForm(request.POST, instance=cat)
    if form.is_valid():
        cat = form.save()
        return HttpResponseRedirect(reverse('cat:show', args=[cat.pk]))
    else:
        return render(request, 'cat/cat_edit.html', locals())
