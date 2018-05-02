from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from loginsys import views




urlpatterns = [


url(r'^login/',views.login, name = 'login'),
url(r'^logout/',views.logout, name = 'logout'),





]