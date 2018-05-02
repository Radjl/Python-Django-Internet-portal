from django.conf.urls import url
from django.urls import path, include

from logistic import views




urlpatterns = [


url(r'^ships_list/$',views.ships_list, name = 'ships'),
url(r'^ships_add/$',views.ships_add, name = 'ships_add'),
    #Убрана строка перед регулярным выражением ships_detail/ для того чтобы не писать перед айди (ниже передаем айди для детализации выбора)
url(r'^(?P<id>\d+)/$',views.ships_detail, name = 'detail'),
url(r'^(?P<id>\d+)/edit/$',views.ships_update, name = 'ships_update'),
url(r'^(?P<id>\d+)/delete/$',views.ships_delete, name = 'ships_delete'),
url(r'^(?P<id>\d+)/comment/$',views.ShipComment, name = 'ships_comment'),
url(r'^(?P<id>\d+)/comment_delete/$',views.comment_delete, name = 'comment_delete'),



url(r'^ships_add2/$',views.ships_add2, name = 'shipadd2'),
url(r'^(?P<id>\d+)/field$',views.ships_update2, name = 'update'),
]