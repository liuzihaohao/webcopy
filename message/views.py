from base64 import encode
from cgitb import text
from email import message
from django.shortcuts import render
from sympy import im, re
from .models import messgaelist,settingslist,filedellist
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import messgaelistdbSerializer,settingslistdbSerializer
import string,random,os
from webcopy.settings import BASE_DIR
from uuid import uuid4
DEL_LIST=[]
def indexhome(request):
    return render(request,'../templates/index.html',{"titles":settingslist.objects.get(key="title").val})

def seachdb(request):
    if request.method=='GET':
        code=request.GET.get("code")
        obj=messgaelist.objects.filter(code=code)
        if obj:
            if messgaelist.objects.get(code=code).typetf=='t':
                t=messgaelist.objects.get(code=code).text
                # messgaelist.objects.get(code=code).delete()
                return render(request,'../templates/index.html',{
                    "bigtext":t,"ifbigtext":"true","titles":settingslist.objects.get(key="title").val,"iftext":True
                })
            else:
                t=messgaelist.objects.get(code=code).file
                # DEL_LIST.append(t)
                # filedellist.objects.create()
                # messgaelist.objects.get(code=code).delete()
                return render(request,'../templates/index.html',{
                    "bigtext":"","ifbigtext":"true","bigfile":'/media/'+str(t),"iftext":False,"titles":settingslist.objects.get(key="title").val
                })
        return render(request,'../templates/index.html',{
            "bigtext":"错误的提取码","ifbigtext":"true"
        })
    return render(request,'../templates/index.html')

def uptext(request):
    if request.method=='POST':
        t=''
        while True:
            t=''.join(random.sample(string.ascii_letters + string.digits, 5))
            if not messgaelist.objects.filter(code=t):
                break
        messgaelist.objects.create(code=t,typetf='t',text=request.POST.get("text"))
        return render(request,'../templates/index.html',{"codes":t,"ifcode":"true","titles":settingslist.objects.get(key="title").val})
    return render(request,'../templates/index.html',{"titles":settingslist.objects.get(key="title").val})
    
def fileup(request):
    if request.method=='POST':
        fobj=request.FILES.get("file",'')
        t=''
        while True:
            t=''.join(random.sample(string.ascii_letters + string.digits, 5))
            if not messgaelist.objects.filter(code=t):
                break
        messgaelist.objects.create(code=t,typetf='f',file=fobj)
        return render(request,'../templates/index.html',{"codes":t,"ifcode":"true","titles":settingslist.objects.get(key="title").val})
    return render(request,'../templates/index.html')

# Create your views here.
class MYPermissions(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (not request.user.is_anonymous)
class messgaelistdbViewSet(viewsets.ModelViewSet):
    queryset = messgaelist.objects.all()
    serializer_class = messgaelistdbSerializer
    permission_classes = [permissions.IsAuthenticated]
class settingslistdbViewSet(viewsets.ModelViewSet):
    queryset = settingslist.objects.all()
    serializer_class = settingslistdbSerializer
    permission_classes = [MYPermissions]