from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"isArama/index.html")

def isarama(request):
    return render(request,"isArama/blogs.html")

def isarama_details(request,id):
    return render(request,"isArama/isAramadetails.html",{
        "id":id
    })
