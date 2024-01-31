from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from app.forms import *


def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topic is done')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insert_webpage is done')
            
    return render(request,'insert_webpage.html',d)   

def  insert_accessrecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}

    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('insert_accessrecord is done')
    return render(request,'insert_accessrecord.html',d)    
