from django.http import HttpResponse
import sys
import  urllib2
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index2.html')


def firstpage(request):
    request = urllib2.Request('https://gupiao.baidu.com/stock/603299.html?from=aladingpc')
    source = urllib2.urlopen(request)
    result = source.read()
    return render(request,'index.html',{'string':result})