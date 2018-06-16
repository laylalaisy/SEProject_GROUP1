from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest,HttpResponse

from basicInfo.models import account

import hashlib as hash,json



@csrf_exempt
def api_account_post(request):
    if request.method=="POST":
        print("fuckyou")
        username=request.POST["account_id"]
        password=request.POST["account_pw"]
        print(username,password,"-----")

        request.session["account_id"]=username
        return JsonResponse({"success": 1, "type": 0, "reason": None},safe=False)

        try:
            obj = account.objects.get(account_id=username)
            passwd = obj.password
            salt = obj.salt
            passwordAfter = hash.sha512((hash.sha512(password.encode()).hexdigest() + salt).encode()).hexdigest()
            if passwordAfter == passwd:
                request.session["account_id"] = username

                return JsonResponse({"success":1,type:obj.type,"reason":None})

            else:
                return JsonResponse({"success":0,type:None,"reason":'密码错误'})

        except:
            return JsonResponse({"success": 0, type: None, "reason": '用户名错误'})

    return HttpResponseBadRequest()
