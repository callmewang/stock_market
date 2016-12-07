from django.http import HttpResponse
import sys
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index2.html')


def firstpage(request):
    return render(request,'index.html')