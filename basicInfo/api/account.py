from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest,HttpResponse

from basicInfo.models import account

import hashlib as hash,json



def api_account_post(request):
    if request.method=="POST":
        print("fuckyou")
        username=request.POST["account_id"]
        password=request.POST["account_pw"]

        try:
            obj = account.objects.get(account_id=username)
            passwd = obj.password
            salt = obj.salt
            passwordAfter = hash.sha512((hash.sha512(password.encode()).hexdigest() + salt).encode()).hexdigest()
            if passwordAfter == passwd:
                request.session["account_id"] = username

                return JsonResponse({"success":1,"type":obj.type,"reason":None})

            else:
                return JsonResponse({"success":0,"type":None,"reason":'密码错误'})

        except:
            return JsonResponse({"success": 0, "type": None, "reason": '用户名错误'})

    return HttpResponseBadRequest()

@csrf_exempt
def api_account_register_post(request):
    '''
    ```doc
    @param
        account_id(string):新建的用户名
        account_pw(string):新建的密码
        accout_type(int):注册账户的类型（学生、老师、管理员）
    @return
        json object{
            success(bool):注册成功与否
            reason(string):不成功的原因
        }
    ```
    :param request:
    :return:
    '''
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
        # if len(username) < 6:
        #     return render(request, 'WebTA/signup.html', {'errorName': "用户名短于6位"})
        # try:
        #     account.objects.get(account_id=username)
        #     return render(request, 'WebTA/signup.html', {"errorName": "用户名已存在"})
        # except:
        #     salt1 = int(time.time() % 100)
        #     salt = "00" if salt1 == 0 else str(salt1)
        #     for i in range(6):
        #         salt += str(
        #             hex(int(random.uniform(0, 16)))
        #         )[2:3]
        #
        #     print(salt)
        #     passwordAfter = hash.sha512((hash.sha512(password.encode()).hexdigest() + salt).encode()).hexdigest()
        #     account.objects.create(account_id=username, password=passwordAfter, salt=salt)
        #     request.session["name"] = username
        #     return HttpResponseRedirect("WebTA/index.html")
        #     pass
    return
