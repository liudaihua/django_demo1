from django.shortcuts import render
from app01 import models
# Create your views here.


def get_classes(request):
    '''

    :param request:
    :return:
    '''

    cls_list=models.Classes.objects.all()
    print(cls_list)
    return render(request,'get_classes.html',{"cls_list":cls_list})



def add_classes(request):
    '''

    :param request:
    :return:
    '''
    return render(request,"add_classes.html")