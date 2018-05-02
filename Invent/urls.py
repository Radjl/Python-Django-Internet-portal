from django.urls import path, include

from Invent import views




urlpatterns = [

path('', views.list, name='inventlist'),
path('test', views.test, name='test'),
path('additem',views.additem, name='additem'),
path('remove_items',views.removeitem, name='remove_item'),
path('edit_items',views.edit_item, name='edit_item'),

]