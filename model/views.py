from django.shortcuts import render

from .models import ModelObjEnvinterface

def index(request):
    objs = ModelObjEnvinterface.objects.all()
    objsLen = len(objs)
    print(objsLen)
    return render(request, 'index.html', locals())
