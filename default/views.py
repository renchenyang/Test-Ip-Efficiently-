# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.shortcuts import redirect
from default.models import Todolist,historydata
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import time,socket,struct

# Create your views here.

@login_required
def getlist(request):
    todolist = Todolist.objects.all()
    for i in todolist:
        if i.state==0:
            i.state="不可达"
        else:
            i.state="可达"
    return render(request,'getlist.html',{'todolist':todolist})

@login_required
def getlist2(request):
    todolist = Todolist.objects.all()
    for i in todolist:
        if i.state==0:
            i.state="不可达"
        else:
            i.state="可达"
    return render(request,'getlist2.html',{'todolist':todolist})

@login_required
def addlist(request):
    if request.method == 'GET':
        return render(request,'addlist.html')
    elif request.method == 'POST':
        f3= request.POST['field3']
        todo = Todolist(ip=f3,state=0)
        todo.save()
        todolist = Todolist.objects.all()
        return redirect('/')

@login_required
def updatelist(request):
    if request.method == 'GET':
        todoid = request.GET['todoid']
        todo = Todolist.objects.get(id=todoid)
        return render(request,'updatelist.html',{'todo':todo})
    elif request.method == 'POST':
        todoid = request.POST['id']
        f3= request.POST['field3']
        todo = Todolist.objects.get(id=todoid)
        todo.ip = f3
        todo.save()
        todolist = Todolist.objects.all()
        return redirect('/')

@login_required
def dellist(request):
    id = request.GET['todoid']
    Todolist.objects.filter(ip=id).delete()
    res ={"success":"true"}
    return JsonResponse(res)


def login2(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(username=username2, password=password2)
        if user is not None:
            if user.is_active:
                login(request,user)
                todolist = Todolist.objects.all()
                for i in todolist:
                    if i.state==0:
                        i.state="不可达"
                    else:
                        i.state="可达"
                if user.is_superuser:
                    return redirect('/')
                else:
                    return redirect('/getlist2')
            else:
                print("The password is valid, but the account has been disabled!")
                return render(request,'login2.html')
        else:
            return render(request,'login2.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/account/login')

@login_required
def todogetlist(request):
    dataset = Todolist.objects.all()
    for i in dataset:
        if i.state==0:
            i.state="不可达"
        else:
            i.state="可达"
    todolist = []
    for item in dataset:
        temp ={"id":item.id,"content":item.state,"ip":item.ip}
        todolist.append(temp)
    res ={"todolist":todolist}
    return JsonResponse(res)

@login_required
def history(request):
    host = request.GET['todoid']
    thehistorydata1 = historydata.objects.filter(ip=host).all()
    for i in thehistorydata1:
        i.state=time.asctime(time.localtime(i.state))
    for i in thehistorydata1:
        if i.time==0:
            i.time="不可达"
        else:
            i.time="可达"
    return render(request,'historydatalist.html',{'thehistorydata':thehistorydata1,'hostnumber':host})

@login_required
def addlist2(request):
    if request.method == 'GET':
        return render(request,'addlist2.html')
    elif request.method == 'POST':
        f3= request.POST['field3']
        packedIP = socket.inet_aton(f3)
        ip_num=struct.unpack("!L", packedIP)[0]
        f4=request.POST['field4']
        netlength = 32-int(f4)
        power=pow(2,netlength)
        ip_num=ip_num/power
        ip_num=ip_num*power
        j=0
        while (j<power):
            ip_ip=socket.inet_ntoa(struct.pack('!L',ip_num))
            todo = Todolist(ip=ip_ip,state=0)
            todo.save()
            j=j+1
            ip_num=ip_num+1
        return redirect('/')

@login_required
def refresh(request):
    address = ('localhost', 9999)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(address)
        s.send('refresh')
        s.close()
    except:
        return redirect('/')
    return redirect('/')