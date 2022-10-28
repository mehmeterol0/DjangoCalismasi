from distutils.log import error
import email
from django.http.response import HttpResponse
from django.shortcuts import render
from matplotlib.style import context
from blog.models import Blog, Category, Basvurular

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User





def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html", {
        "blog": blog
    })

def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)

def is_basvurulari(request):
    if request.method == 'POST':
       q = Basvurular(
           email=request.POST.get("email"), 
           onyazi=request.POST.get("onyazi"), 
           cv=request.POST.get("cv"), 
       )
       q.save()
    return render(request,'blog/blogs.html',locals())
