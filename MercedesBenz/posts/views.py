from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
    return HttpResponse('<h2>welcome to my fucking sajfijhsfg</h2>')


def homemenu(request):
    menutemplate = loader.get_template('posts/menuhome.html')
    return HttpResponse(menutemplate.render())