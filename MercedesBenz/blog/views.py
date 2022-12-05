from django.shortcuts import render
from .models import Blog

def Bloglistview(request):
    bloglist = Blog.objects.all()

    context = {
        "BlogListDic":  bloglist
    }

    return render(request , "bloglists.html" , context )