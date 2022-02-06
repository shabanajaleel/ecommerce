from django.shortcuts import render,redirect
from . forms import CustomUserForm, RoleForm
from . models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,get_user_model

User=get_user_model()
# Create your views here.
def fnaddroles(request):
    form=RoleForm()
    if request.method=="POST":
        form=RoleForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render (request,'admin/addrole.html',context)

def fnroles(request):
    roles=Role.objects.all()
    context={'roles':roles}
    return render(request,'admin/roles.html',context)

def fndeleteroles(request,role_id):
    roles=Role.objects.get(id=role_id)
    roles.delete()
    return redirect(fnroles)

def fnaddadmin(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        print(form)
        if form.is_valid():
            user=form.save()
            messages.success(request,'data inserted successfully')
            return redirect(fnaddadmin)
    return render(request,'admin/addadmin.html',{'form':form})

def fnviewadmin(request):
    admin=User.objects.all()
    context={'admin':admin}
    return render(request,'admin/viewadmin.html',context)

def fnlogin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        print(uname)
        password=request.POST['password']
        print(password)
        user=authenticate(username=uname,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return render(request,'admin/roles.html')
    return render(request,'admin/login.html')

