from django.shortcuts import render, redirect, render_to_response

# Create your views here.
import output as output
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.context_processors import csrf
from django.views.generic import TemplateView
from django_tables2 import RequestConfig
from django.contrib import auth





def login(request):
    page = request.POST.get('next')
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)


            return redirect(request.POST.get('next'))






        else:
            args['login_error'] = 'Пользователь не найден'
            return redirect(request.POST.get('next'), args)




    return render(request,'login.html')









def logout(request):
    auth.logout(request)
    return redirect("/")


