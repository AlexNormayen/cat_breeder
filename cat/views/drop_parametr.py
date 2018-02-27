#!/usr/bi/env pethon3
#-*- coding: utf-8 -*-


from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from ..models import Cat, Parametr


from django.db import connection
from textwrap import dedent

def drop_parametr(request, id_cat, pk_parametr):
    with connection.cursor() as cursor:
        cursor.execute(
            dedent('''\
                delete 
                    from cat_cat_parametrs 
                    where cat_id = %s
                        and parametr_id = %s;'''),
            [ id_cat, pk_parametr ]
        )
    return HttpResponseRedirect(reverse('cat:parametrs', args=[id_cat]))




def drop_parametr_для_ламеров(request, id_cat, pk_parametr):
    cat = get_object_or_404(Cat, pk=id_cat)
    parametr = get_object_or_404(Parametr, pk=pk_parametr)
    cat.parametrs.remove(parametr)
    cat.save()
    return HttpResponseRedirect(reverse('cat:parametrs', args=[id_cat]))

