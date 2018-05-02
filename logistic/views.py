from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator
# Create your views here.
from logistic.models import Ship,Comment
from logistic.forms import ShipAdd,CommentForm,shipadd2
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required(login_url='/auth/login/')
def ships_list(request):
    allships = Ship.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        allships = allships.filter(Name__icontains=query)

    page = request.GET.get('page')

    paginator = Paginator(allships, 4)  # Show 25 contacts per page


    try:
        allships = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        allships = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        allships = paginator.page(paginator.num_pages)


    return render(request,'shipshome.html', {"allships": allships})


def ships_add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ShipAdd(request.POST or None , request.FILES or None)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['Name']
            Photo = form.cleaned_data['Photo']
            Info = form.cleaned_data['Info']
            Content = form.cleaned_data['Content']
            ContentEng = form.cleaned_data['ContentEng']
            PubDate = timezone.now()

            a = Ship(Name=name,Photo=Photo,Info=Info,Content=Content,ContentEng=ContentEng,Pubdate=PubDate)
            a.save()
            messages.success(request,'Создано успешно')
            return HttpResponseRedirect('/logistic/ships_list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ShipAdd()
        return render(request, 'addship.html', {'form': form})








def ships_detail(request,id):
    instance = get_object_or_404(Ship, id = id)
    formcomment = CommentForm
    addform = ShipAdd


    context = {'ship':instance,
                'commentform':formcomment,
               'addform':addform
               }
    return render(request,'shipdetail.html',context)




def ships_delete(request, id=None):
    instance = get_object_or_404(Ship, id = id)
    instance.delete()
    messages.info(request, 'Запись удалена')
    return redirect('/logistic/ships_list/')




def ships_update(request, id=None):
    instance = get_object_or_404(Ship, id = id)
    form = ShipAdd(request.POST or None , request.FILES or None)
    if form.is_valid():
        name = form.cleaned_data['Name']
        Info = form.cleaned_data['Info']
        Content = form.cleaned_data['Content']
        ContentEng = form.cleaned_data['ContentEng']
        PubDate = timezone.now()


        instance.Name = name
        instance.Info = Info
        instance.Content = Content
        instance.ContentEng = ContentEng
        instance.Pubdate = PubDate
        instance.save()
        context = {'ship': instance}
        messages.success(request,'Успешно отредактировано')
        return render(request,'shipdetail.html',context)
    else:
        form = ShipAdd()
        return render(request, 'addship.html', {'form': form})

def ships_update2(request, id=None):
    instance = get_object_or_404(Ship,id=id)
    form = shipadd2(request.POST or None , request.FILES or None , instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/logistic/ships_list/')

    context = {'instance':instance,'form':form,'ship':instance}
    return render(request,'shipedit.html',context)







def ShipComment(request, id):
    ship = get_object_or_404(Ship, id=id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment()
        comment.post = ship
        comment.text = form.cleaned_data['Content']
        comment.ContentExtended = form.cleaned_data['ContentExtended']
        comment.save()

        context = {'ship':ship}
        return render(request,'shipdetail.html',context)



    else:
        form = CommentForm()
    return render(request, 'addship.html', {'form': form})


def comment_delete(request,id=None):
    instance = get_object_or_404(Comment, id=id)
    instance.delete()
    messages.info(request, 'Запись удалена')


    return redirect('/logistic/ships_list/')


def ships_add2(request):
    if request.method == 'POST':
        form = ShipAdd(request.POST or None, request.FILES or None)
        if form.is_valid():
            name = form.cleaned_data['Name']
            Photo = form.cleaned_data['Photo']
            Info = form.cleaned_data['Info']
            Content = form.cleaned_data['Content']
            ContentEng = form.cleaned_data['ContentEng']
            PubDate = timezone.now()

            a = Ship(Name=name, Photo=Photo, Info=Info, Content=Content, ContentEng=ContentEng, Pubdate=PubDate)
            a.save()
            messages.success(request, 'Создано успешно')
            return HttpResponseRedirect('/logistic/ships_list/')


    else:
        form = ShipAdd()
        return render(request, 'addship.html', {'form':form})




















