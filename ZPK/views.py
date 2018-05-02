import output as output
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django_tables2 import RequestConfig
from django.contrib import auth


from ZPK.models import Worker, PhoneBook


def index(request):
    return render(request,'polls/index.html',{'username':auth.get_user(request).username})



def list(request):
    all_workers = Worker.objects.all()
    context = {'allworkers': all_workers}
    return render(request,'polls/list.html',context)

def workerlist2(request, worker_id):
    worker = Worker.objects.get(pk=worker_id)
    context = {'worker':worker}
    return render(request,'polls/list.html',context)


def menu(request):

  #  if auth.get_user(request).is_authenticated:
        return render(request, 'polls/menu.html', {'username': auth.get_user(request).username})
   # else:
    #    return render(request,'polls/index.html',{'username':auth.get_user(request).username})




def menu2(request):
    all_workers = Worker.objects.all()
    context = {'allworkers': all_workers}
    return render(request,'polls/menu.html',context)



def test(request):
    return render(request,'polls/test.html')

def test2(request):
    all_workers = Worker.objects.all()
    context = {'allworkers': all_workers}
    return render(request,'polls/test.html',context)


def allphones(request):

    return render(request,'polls/menu.html',{'allphones':PhoneBook.objects.all()})


def index2(request):
    return render(request,'polls/index2.html')