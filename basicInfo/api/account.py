from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest,HttpResponse

from basicInfo.models import account

import hashlib as hash,json,time,random


@csrf_exempt
def api_account_post(request):
    if request.method=="POST":
        print("fuckyou")
        username=request.POST["account_id"]
        password=request.POST["account_pw"]
        print(username,password)

        try:
            obj = account.objects.get(account_id=username)
            print("----")
            passwd = obj.password
            salt = obj.salt
            passwordAfter = hash.sha512((hash.sha512(password.encode()).hexdigest() + salt).encode()).hexdigest()
            print(passwd,passwordAfter)
            if passwordAfter == passwd:
                request.session["account_id"] = username

                return JsonResponse({"success":1,"type":obj.type,"reason":None})

            else:
                return JsonResponse({"success":0,"type":None,"reason":'密码错误'})

        except:
            print("===")
            return JsonResponse({"success": 0, "type": None, "reason": '用户名错误'})

    return HttpResponseBadRequest()

@csrf_exempt
def api_account_register_post(request):
    if request.method=="POST":
        username = request.POST.get("account_id", '')
        password = request.POST.get("account_pw", '')
        type=request.POST.get("accout_type",0)

        print(username, password,type)
        if (len(password) < 6 or len(password) > 18):
            return JsonResponse({
                "success":0,
                "reason":"密码长度不符合要求"
            })

        if len(username) < 6:
            return JsonResponse({
                "success":0,
                "reason":"用户名短于6位"
            })
        try:
            account.objects.get(account_id=username)
            return JsonResponse({
                "success": 0,
                "reason": "用户名已存在"
            })
        except:
            salt1 = int(time.time() % 100)
            salt = "00" if salt1 == 0 else str(salt1)
            for i in range(6):
                salt += str(
                    hex(int(random.uniform(0, 16)))
                )[2:3]

            print(salt)
            passwordAfter = hash.sha512((hash.sha512(password.encode()).hexdigest() + salt).encode()).hexdigest()
            account.objects.create(account_id=username, password=passwordAfter, salt=salt)

            request.session["account_id"] = username
            return JsonResponse({
                "success": 1,
                "reason": None
            })
    return HttpResponseBadRequest

@csrf_exempt
def api_account_repassword_post(request):
    '''
    ##### POST /api/account/repassword

    账户密码修改

    ```doc
    @param
        account_id(string):当前的用户名
        account_pw(string):新建的密码
    @return
        json object{
            success(bool):修改成功与否
            reason(string):不成功的原因
        }
    ```
    :param request:
    :return:
    '''

    if request.method=="POST":
        account_id=request.POST.get("account_id","")
        account_pw=request.POST.get("account_pw","")
        try:
            obj=account.objects.get(account_id=account_id)
            if(len(account_pw)<6 or len(account_pw)>18):
                return JsonResponse({
                    "success":0,
                    "reason":"密码长度不符合要求"
                })

            salt1 = int(time.time() % 100)
            salt = "00" if salt1 == 0 else str(salt1)
            for i in range(6):
                salt += str(
                    hex(int(random.uniform(0, 16)))
                )[2:3]

            print(salt)
            passwordAfter = hash.sha512((hash.sha512(account_pw.encode()).hexdigest() + salt).encode()).hexdigest()
            obj.password=passwordAfter
            obj.save()
            return JsonResponse({
                "success":1,
                "reason":None
            })

        except:
            return HttpResponseNotFound()

@csrf_exempt
def api_account_person_post(request):
    '''
    account_id(string):当前的用户名
	name(string):真实姓名
    nick(string):昵称
    email(string):电子邮箱
    exp(int):个人经验
    coin(int):金币数
    :param request:
    :return:
    '''
    try:
        account_id=request.POST["account_id"]
        name=request.POST["name"]
        nick=request.POST["nick"]
        email=request.POST["email"]
        exp=request.POST["exp"]
        coin=request.POST["coin"]

        return JsonResponse({"success":1,"reason":None})

    except:
        return HttpResponseBadRequest()


@csrf_exempt
def api_account_person_get(request):
    '''
    json object{
		name(string):真实姓名
		nick(string):昵称
		email(string):电子邮箱
		exp(int):个人经验
		coin(int):金币数
		//...(还有什么别的个人信息随便加)
	}
    :param request:
    :return:
    '''
    return JsonResponse(
        {
            "name":"Alan Swift",
            "nick":"Shina Mashiro",
            "email":"123456@163.com",
            "exp":100,
            "coin":90
        }
    )

@csrf_exempt
def api_account_person(request):
    if request.method=="POST":
        return api_account_person_post(request)
    else:
        return api_account_person_get(request)

