 

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.db import connection
from restful import restful
from ..forms import PictureForm


def picture(request, id_cat):
    with connection.cursor() as cursor:
        cursor.execute(
            'select picture from cat_cat where id = %s ;',
            [ id_cat]
        )
        ( data, ) = cursor.fetchone()
    if not data: 
        raise Http404()
    
    response = HttpResponse(content_type='image/jpeg')
    response.write(data)
    return response




@restful
def add_picture(request, id_cat):
    form = PictureForm()
    return render(request, 'cat/cat_picture.html', locals())

@add_picture.method("POST")
def add_picture(request, id_tovar):
    form = PictureForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'cat/cat_picture.html', locals())
    data = b''
    for chunk in request.FILES['picture'].chunks():
        data += chunk
    with connection.cursor() as cursor:
        cursor.execute('update cat_cat set picture=%s where id=%s ;',
                       [data, id_cat]
                    )
    return HttpResponseRedirect(reverse('cat:index'))
    
