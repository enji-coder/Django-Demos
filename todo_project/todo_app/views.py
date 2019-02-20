from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
        title="<h4><b>user data</b></h4>"
        name="<b><p> Enter Name </p><b>"

        return render(request,"todo_app/insert.html",{'name':name,'title':title})

def storeData(request):
    obj=tbl_data()
    obj.name = request.POST['name']
    obj.email = request.POST['email']
    obj.mobile = request.POST['mobile']
    newdata = tbl_data.objects.create(name = obj.name, email= obj.email,mobile=obj.mobile )
    if newdata:  
        result=tbl_data.objects.all()
        return render(request,'todo_app/showlist.html',{'result':result})
