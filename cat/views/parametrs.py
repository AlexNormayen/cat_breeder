 
from textwrap import dedent
from django.shortcuts import get_object_or_404, render
from django.db import connection
from ..models import Cat, Parametr
from ..forms import ParametrListForm 
from restful import restful




@restful
def parametrs(request, id_cat):
    cat = get_object_or_404(Cat, pk=id_cat)
    form = ParametrListForm
    return render(request, 'cat/parametrs.html', locals())


@parametrs.method('POST')
def parametrs(request, id_cat):
    form = ParametrListForm(request.POST)
    if form.is_valid():
        tag_list = form.cleaned_data['parametr_list']
        tag_list = parametr_list.split(',')
        tag_list = map(str.strip, parametr_list)
        tag_list = map(str.lower, parametr_list)
        with connection.cursor() as cursor:
            for pk_parametr in parametr_list:
                cursor.execute(dedent('''\
                    insert into cat_parametr (breed)
                        values( %s )
                        on conflict do nothing ;'''),
                    [ pk_parametr ]
                )
                cursor.execute(dedent('''\
                    insert into cat_cat_parametrs ( cat_id, parametr_id)
                        values( %s, %s)
                        on conflict do nothing ;'''),
                    [ id_cat, pk_parametr ]
                )
            
           
    cat = get_object_or_404(Cat, pk=id_cat)
    return render(request, 'cat/parametrs.html', locals())


#def tags_for_lamers(request, id_cat):
#    form = ParametrListForm(request.POST)
#    if form.is_valid():
#        parametr_list = form.cleaned_data['parametr_list']
#        cat = get_object_or_404(Cat, pk=id_cat)
#        for pk_parametr in map(str.strip,parametr_list.split(',')):
#            pk_parametr = pk_parametr.lover()
#            try:
#                parametr = Parametr.objects.get(pk=pk_parametr)
#            except Parametr.DoesNotExist:
#                parametr = Parametr(title=pk_parametr)
#                parametr.save()                
#            cat.parametrs.add(parametr)
#        cat.save()
#    return render(request, 'cat/parametrs.html', locals())
    
#    tovar = get_object_or_404(Cat, pk=id_cat)
#    form = ParametrListForm
#    return render(request, 'cat/parametrs.html', locals())
