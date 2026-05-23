from django.http import HttpResponse
from django.shortcuts import render
from .models import department

def home(request):
    return render(request,'home.html')

def colleges(request):
    college_list=['SVECW','VIT','BVRIT']
    return render(request,'colleges.html',{'colleges':college_list})


def students(request):
    data=[{'sno':1,'name':'Asha','branch':'CSE','age':19},{'sno':2,'name':'Amy','branch':'ECE','age':17},{'sno':3,'name':'Ankitha','branch':'IT','age':20},]
    return render(request,'students.html',{'students':data})
def address(request):
    return render(request, 'address.html')
def db(request):
      s1=department.objects.values_list()
      print(s1)
      return render(request,"app1/app1.html",{"data":s1,})