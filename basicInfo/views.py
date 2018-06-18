from django.shortcuts import render

# Create your views here.


def default(request):
    return render(request, 'login-home.html', {})


def signup(request):
    return render(request, "signup.html", {})

def login(request):
    return render(request,"login.html",{})

def student(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id":sid
    }
    return render(request,"student.html",feedDict)

def teacher(request):
    tid=request.session["account_id"]
    feedDict={
        "account_id":tid
    }
    return render(request,"teacher_information.html",feedDict)