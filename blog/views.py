from django.shortcuts import render
from .forms import LoginPostForm
from django.shortcuts import redirect
from .models import account
from .models import operation
# Create your views here.

def default(request):
    return render(request,'WebTA/login-home.html',{})





def login(request):
    if request.method=="POST":
        username=request.POST.get('account_id','')
        password=request.POST.get('password','')
        try:
            try:
                re=account.objects.get(account_id=username,password=password)
                request.session["name"] = username
                return render(request, "WebTA/index.html", {'account_id': username})
            except:
                return render(request,'WebTA/login.html',{'errorPassword':'密码错误'})
        except Exception as e:
            print(e)
            return render(request, 'WebTA/login.html', {'errorName': '用户名错误'})


    return render(request,'WebTA/login.html',{})

def index(request):
    account_id=request.session["name"]
    return render(request,"WebTA/index.html",{'account_id':account_id})