#!/usr/bi/env pethon3
#-*- coding: utf-8 -*-


from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from ..models import Cat

def delete(request, id_cat):
    cat = get_object_or_404(Cat, pk=id_cat)
    cat.delete()
    return HttpResponseRedirect(reverse('cat:index'))
