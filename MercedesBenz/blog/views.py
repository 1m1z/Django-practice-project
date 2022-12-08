from django.shortcuts import render
from .models import Blog

def Bloglistview(request):
    bloglist = Blog.objects.all()

    context = {
        "BlogListDic":  bloglist
    }

    return render(request , "blog/bloglists.html" , context )

def BlogListDetailsVeiw(request,post_id):
    postmost = Blog.objects.get(pk = post_id)

    context={
        "postdetails": postmost
    }

    return render(request,"blog/blogdetails.html", context)