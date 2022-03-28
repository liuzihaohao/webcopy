from django.shortcuts import render
from .models import messgaelist
import string,random
def indexhome(request):
    return render(request,'../templates/index.html',{})

def seachdb(request):
    if request.method=='GET':
        code=request.GET.get("code")
        obj=messgaelist.objects.filter(code=code)
        if obj:
            if messgaelist.objects.get(code=code).typetf=='t':
                t=messgaelist.objects.get(code=code).text
                messgaelist.objects.get(code=code).delete()
                return render(request,'../templates/index.html',{
                    "bigtext":t,"ifbigtext":True,"iftext":True
                })
            else:
                t=messgaelist.objects.get(code=code).file
                return render(request,'../templates/index.html',{
                    "bigtext":"","ifbigtext":True,"bigfile":'/media/'+str(t),"iftext":False
                })
        return render(request,'../templates/index.html',{
            "bigtext":"错误的提取码","ifbigtext":True,"iftext":True
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
        return render(request,'../templates/index.html',{"codes":t,"ifcode":True})
    return render(request,'../templates/index.html',{})
    
def fileup(request):
    if request.method=='POST':
        fobj=request.FILES.get("file",'')
        t=''
        while True:
            t=''.join(random.sample(string.ascii_letters + string.digits, 5))
            if not messgaelist.objects.filter(code=t):
                break
        messgaelist.objects.create(code=t,typetf='f',file=fobj)
        return render(request,'../templates/index.html',{"codes":t,"ifcode":True})
    return render(request,'../templates/index.html')
