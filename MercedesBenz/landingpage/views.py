#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import CartModel,MotortModel


def indexcar(request):
    car = CartModel.objects.all()
    
    context={
        "Carttitle":car
    }

    return render(request,"cars.html",context )
    # return HttpResponse(template.render(context, request))


def motorlistview(request):
    motor = MotortModel.objects.all()

    context={
        "motordic" : motor
    }

    return render(request,"motors.html",context)