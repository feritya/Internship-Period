from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib.auth.models import User



def home(request):
    if request.user.is_authenticated:
        context={   
            'isim':request.user.username,
            'yas':25,
            'sehir':'İstanbul',
            'meslek':'Yazılım Mühendisi',
        }
    else:
        context={
            'isim':'Misafir',
            'yas':25,
            'sehir':'İstanbul',
            'meslek':'Yazılım Mühendisi',
        }
    return render(request,'home.html',context)
    