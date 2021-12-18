from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"home.html",{'name':'Saurabh'})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    op = request.GET['operation']
    if(op=='add'):
        res = val1 + val2
    elif op=='mul':
        res = val1*val2
    elif op=='sub':
        res = val1-val2
    else:
        if val2 == 0:
            res ="undefine"
        else:
            res = val1/val2
    return render(request,"result.html",{'result' : res})