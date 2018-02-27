


from  django.urls import path

from . import views

app_name = 'cat'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:id_catr>/', views.show, name = 'show'),
    path('<int:id_cat>/edit/', views.edit, name='edit'),
    path('<int:id_cat>/delete/', views.delete, name='delete'),
    path('<int:id_cat>/parametrs/', views.parametrs, name='parametrs'),
    path('<int:id_cat>/<str:pk_parametr>/drop/', views.drop_parametr, name='drop_parametr'),
    path('<int:id_parametr>/add_picture/', views.add_picture, name='add_picture'),
    path('<int:id_cat>/picture/', views.picture, name='picture'),
    path('create/', views.create, name='create'),
    path('groups/', views.group_index, name ='allgroups'),
    
    
    
]
