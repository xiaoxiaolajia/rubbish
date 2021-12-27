from django.http import HttpResponse
from django.shortcuts import render
from model.models import ModelObjEnvinterface
from django.contrib import messages
import time
import model
import string
from datetime import datetime
def hello(request):
    context  = {}
    context['hello'] = 'Hello World!'
    return render(request, 'rubbish.html', context)


def show(request):
    objs = ModelObjEnvinterface.objects.all()
    objsLen = len(objs)
    print(objsLen)
    return render(request, 'show.html', locals())

def login(request):
    return render(request, 'login.html', locals())

def search(request):
    return render(request, 'search.html', locals())

def dosearch(request):
    startTime = request.GET.get('start')
    endTime = request.GET.get('end')
    # address = request.GET.get('address')
    s = datetime.fromisoformat(startTime)
    e = datetime.fromisoformat(endTime)
    # print(s, e)
    lengan = ModelObjEnvinterface.objects.filter(readtime__gte=datetime(s.year, s.month, s.day, s.hour, s.minute, s.second),
                                               readtime__lte=datetime(e.year, e.month, e.day, e.hour, e.minute, e.second),
                                               garabtype='干垃圾').count()
    lengshi = ModelObjEnvinterface.objects.filter(readtime__gte=datetime(s.year, s.month, s.day, s.hour, s.minute, s.second),
                                               readtime__lte=datetime(e.year, e.month, e.day, e.hour, e.minute, e.second),
                                               garabtype='湿垃圾').count()
    lencanchu = ModelObjEnvinterface.objects.filter(readtime__gte=datetime(s.year, s.month, s.day, s.hour, s.minute, s.second),
                                               readtime__lte=datetime(e.year, e.month, e.day, e.hour, e.minute, e.second),
                                               garabtype='餐厨垃圾').count()
    lenchuyu = ModelObjEnvinterface.objects.filter(readtime__gte=datetime(s.year, s.month, s.day, s.hour, s.minute, s.second),
                                               readtime__lte=datetime(e.year, e.month, e.day, e.hour, e.minute, e.second),
                                               garabtype='厨余垃圾').count()
    # print(lengan, lengshi, lencanchu, lenchuyu)

    garabtypes = ['干垃圾', '湿垃圾', '厨余垃圾', '餐厨垃圾']
    counts = [lengan, lengshi, lencanchu, lenchuyu]
    return render(request, 'show.html', locals())

def delete(request):
    return render(request, 'delete.html', locals())

def dodelete(request):
    startTime = request.GET.get('start')
    endTime = request.GET.get('end')
    address = request.GET.get('address')
    grabtype = request.GET.get('garabtype')
    s = datetime.fromisoformat(startTime)
    e = datetime.fromisoformat(endTime)
    try:
        res = ModelObjEnvinterface.objects.filter(readtime__gte=datetime(s.year, s.month, s.day, s.hour, s.minute, s.second),
                                               readtime__lte=datetime(e.year, e.month, e.day, e.hour, e.minute, e.second),
                                               garabtype=grabtype, address=address).delete()
    except:
        messages.add_message(request, messages.ERROR, '抱歉，数据删除失败。')
    else:
        messages.add_message(request, messages.SUCCESS, "数据删除成功！")
    print(messages)
    return render(request, 'delete.html', locals())

def add(request):
    return render(request, 'add.html', locals())

def doadd(request):
    startTime = request.GET.get('time')
    address = request.GET.get('address')
    grabtype = request.GET.get('garabtype')
    weight = request.GET.get('weight')
    carno = request.GET.get('carno')
    s = datetime.fromisoformat(startTime)
    try:
        res = ModelObjEnvinterface.objects.create(readtime=datetime(s.year, s.month, s.day, s.hour, s.minute, s.second),
                                               garabtype=grabtype, address=address, loadweight=int(weight), carLicenseno=carno)
    except Exception as e:
        print(e)
        messages.add_message(request, messages.ERROR, '抱歉，数据添加失败。')
    else:
        messages.add_message(request, messages.SUCCESS, "数据添加成功！")
    return render(request, 'add.html', locals())


def system(request):
    return render(request, 'system.html', locals())