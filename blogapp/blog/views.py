from distutils.log import error
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category

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

def isBasvuru_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        emailtext = request.POST["emailtext"]
        onyazitext = request.POST["onyazitext"]
        cvFile = request.POST["cvFile"]

        if emailtext == "":
            if User.objects.filter(emailtext=emailtext).exists():
                return render(request, "blog-details.html", 
                {
                    "error":"E- Mail Boş Bırakılmaz"
                })

        if onyazitext == "":
            if User.objects.filter(onyazitext=onyazitext).exists():
                return render(request, "blog-details.html", 
                {
                    "error":"Ön Yazı Boş Bırakılmaz"
                })

        if cvFile == "":
            if User.objects.filter(cvFile=cvFile).exists():
                return render(request, "blog-details.html", 
                {
                    "error":"CV'siz Başvuru Yapamazsın."
                })
    
    
    return redirect("home")
