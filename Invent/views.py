import output as output
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import TemplateView
from Invent.models import Inventory

from Invent.models import Inventory
from Invent.forms import InventAddForm












@login_required(login_url='/auth/login/')
def list(request):
    all = Inventory.objects.all()
    context = {'all': all}
    return render(request, 'list.html', context)















def test(request):
    all = Inventory.objects.all()
    context = {'all': all}
    return render(request, 'test.html',context)



def additem(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InventAddForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['Name']
            account = form.cleaned_data['Account']
            lifetime = form.cleaned_data['Lifetime']
            comissioning = form.cleaned_data['Comissioning']
            mol = form.cleaned_data['MOL']
            invnum = form.cleaned_data['InvNum']
            factorynum = form.cleaned_data['FactoryNum']
            location = form.cleaned_data['Location']

            a = Inventory(Name=name,Account=account,Lifetime=lifetime,Comissioning=comissioning,MOL=mol,InvNum=invnum,FactoryNum=factorynum,Location=location)
            a.save()
            return HttpResponseRedirect('/invent/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InventAddForm()

    return render(request, 'name.html', {'form': form})

# Удаление записи на форме
def removeitem(request):
    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        itemfordel = Inventory.objects.get(id=item_id)
        itemfordel.delete()
        return HttpResponseRedirect('/invent/')


def edit_item(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InventAddForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            id = form.cleaned_data['Id']
            name = form.cleaned_data['Name']
            account = form.cleaned_data['Account']
            lifetime = form.cleaned_data['Lifetime']
            comissioning = form.cleaned_data['Comissioning']
            mol = form.cleaned_data['MOL']
            invnum = form.cleaned_data['InvNum']
            factorynum = form.cleaned_data['FactoryNum']
            location = form.cleaned_data['Location']

            a = Inventory.objects.get(pk=id)
            a.Name = name
            a.Account = account
            a.Lifetime = lifetime
            a.Comissioning = comissioning
            a.MOL = mol
            a.InvNum = invnum
            a.FactoryNum = factorynum
            a.Location = location
            a.save()
            return HttpResponseRedirect('/invent/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InventAddForm()

    return render(request, 'name.html', {'form': form})


