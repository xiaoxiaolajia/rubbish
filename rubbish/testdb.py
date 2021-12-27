# -*- coding: utf-8 -*-

from django.http import HttpResponse

from model.models import ModelObjEnvinterface


# 数据库操作
def testdb(request):
    response = ModelObjEnvinterface.objects.get(interfaceid=6721390) #[object类]
    r = response.carLicenseno
    print(r)
    return HttpResponse(r)

def testdb1(request):
    response = ModelObjEnvinterface.objects.get(lienceno=123)
    r = response.carLicenseno
    return HttpResponse(r)

def testdb2(request):
    response1 = ModelObjEnvinterface.objects.insert(lienceno=543)
    r = response1.carLicenseno
    response2 = ModelObjEnvinterface.objects.delete(lienceno=41232)
    return HttpResponse(r+response2)

def testdb3(request):
    response = ModelObjEnvinterface.objects.delete(interfaceid=6721390)
    r = response.carLicenseno
    return HttpResponse(r)

def testdb4(request):
    response = ModelObjEnvinterface.objects.get(datatime=2020.12)
    r = response.carLicenseno
    return HttpResponse(r)

def testdb5(request):
    response = ModelObjEnvinterface.objects.get(parname="徐汇区")

    return HttpResponse(response)


