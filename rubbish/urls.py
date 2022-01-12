"""rubbish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views, testdb
urlpatterns = [
    path('hello/', views.hello),
    path('testdb/', testdb.testdb),
    path('show/', views.show),
    path('search/', views.search),
    path('dosearch/', views.dosearch),
    path('delete/', views.delete),
    path('dodelete/', views.dodelete),
    path('login/', views.login),
    path('system/', views.system),
    path('add/', views.add),
    path('doadd/', views.doadd),
    path('complete/', views.complete),
    path('docomplete/', views.docomplete),
    url(r'^$', views.login)
]
