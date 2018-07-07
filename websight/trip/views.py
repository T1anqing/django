from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
# Create your views here.
from . import models

def index(request):
    return render(request, 'trip/index.html')


def test(request):
    contact_list = models.Ctrip.objects.all()
    paginator = Paginator( contact_list, 6 )  # Show 25 contacts per page

    page = request.GET.get( 'page' )
    try:
        contacts = paginator.page( page )  ######存放每页信息的数组
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page( paginator.num_pages )

    return render( request, 'trip/test.html', locals() )

def city(request):
    citys = models.Place.objects.all()
    paginator = Paginator( citys, 4 )  # Show 25 contacts per page

    page = request.GET.get( 'page' )
    try:
        contacts = paginator.page( page )
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page( paginator.num_pages )
    return render(request,'trip/city_page.html',locals())

def scenicspot(request,city):
    citys = models.Place.objects.all()
    Ctrips = models.Ctrip.objects.filter(inplace_pinyin=city ).order_by( '-score' )
    Mafengwos = models.Mafengwo.objects.filter( inplace_pinyin=city )
    paginator = Paginator( Ctrips, 6 )  # Show 25 contacts per page

    page = request.GET.get( 'page' )
    try:
        contacts = paginator.page( page )  ######存放每页信息的数组
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page( paginator.num_pages )
    return render( request, 'trip/place_page.html', locals() )


def place(request,place):
    Ctrip = models.Ctrip.objects.get(title_pinyin=place)
    Mafengwo = models.Mafengwo.objects.filter(title_pinyin=place)
    return render(request,'trip/concrete.html',locals())


# def place(request,place):
#     Ctrip = models.Ctrip.objects.get(title_pinyin=place)
#     Mafengwo = models.Mafengwo.objects.filter(title_pinyin=place)
#     return render(request,'trip/last.html',{'Ctrip':Ctrip,'Mafengwo': Mafengwo})

def about(request):
    return render(request, 'trip/about.html')


def contact(request):
    return render(request, 'trip/contact.html')

















# def index(request):
#     places = models.Place.objects.all()
#     return render(request,'trip/index.html',{'places': places})
#
#
# def about(request):
#     places = models.Place.objects.all()
#     return render(request, 'trip/1.html', {'places': places})
#
#
# def place(request,place):
#     places = models.Place.objects.all()
#     Ctrip = models.Ctrip.objects.filter(inplace_pinyin=place).order_by('-score')
#     Mafengwo = models.Mafengwo.objects.filter(inplace_pinyin=place)
#     return render(request,'trip/place_page.html',{'Ctrip':Ctrip,'Mafengwo': Mafengwo,'places':places})
#
#
# def sight(request,b):
#     Ctrip = models.Ctrip.objects.get(title_pinyin=b)
#     Mafengwo = models.Mafengwo.objects.filter(title_pinyin=b)
#     return render(request,'trip/sight_page.html',{'Ctrip':Ctrip,'Mafengwo': Mafengwo})
#
#
# def contact(request):
#     places = models.Place.objects.all()
#     return render(request,'trip/contact.html',{'places':places})
