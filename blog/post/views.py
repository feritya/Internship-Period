from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *


def post_index(request):
    posts=Post.objects.all()
    return render (request,'post/index.html',{'posts':posts})

def post_detail(request,post_id):
    posts=get_object_or_404(Post,id=post_id)
    context={

        'posts':posts,

    }
    return render(request,'post/detail.html',context)


def post_create(request):
    return HttpResponse("<h1>OLUSTUR</h1><div><h2>olusturdasaniz</h2></div>")


def post_update(request):
    return HttpResponse("<h1>GUNCELLE</h1><div><h2>guncelledasaniz</h2></div>")


def post_delete(request):
    return HttpResponse("<h1>SIL</h1><div><h2>sil'dasaniz</h2></div>")
