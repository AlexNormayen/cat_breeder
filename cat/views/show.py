 

from django.shortcuts import render, get_object_or_404

from ..models import Cat






def show(request, id_cat):
    
    cat = get_object_or_404(Cat, pk=id_cat)    
    
    parametrs = ', '.join( parametr.breed for parametr in cat.parametrs.all() )
    
    
    return render(request, 'cat/cat_show.html', locals())
