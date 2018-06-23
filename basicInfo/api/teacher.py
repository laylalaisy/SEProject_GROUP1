from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponse

from basicInfo.models import account, examination, takeup, teach, course, room, learn, teacher, student,attrib

@csrf_exempt
def api_teacher_info(request):
    if request.method == "GET":
        try:
            print("------")
            account_id = request.GET["account_id"]
            print(account_id)

            teacher_info=teacher.objects.get(teacher_id=account_id)

            print(teacher_info)

            teacher_attrib_info=attrib.objects.get(account_id=account_id)
            print(teacher_attrib_info)

            ret={}
            ret["name"]=teacher_info.name
            print(ret)
            ret["teacher_title"]=teacher_info.title
            ret["teacher_office"]=teacher_info.office
            ret["teacher_management"]=teacher_info.management
            ret["email"]=teacher_attrib_info.email

            return JsonResponse(ret)

        except:
            return HttpResponseBadRequest()
    else:
        print("fuck")
        ret={}
        try:
            account_id=request.POST["account_id"]
            account_email=request.POST["account_email"]
            teacher_office=request.POST["teacher_office"]

            teacher_info = teacher.objects.get(teacher_id=account_id)
            teacher_attrib_info = attrib.objects.get(account_id=account_id)

            print(teacher_info,teacher_attrib_info)
            teacher_info.office=teacher_office
            teacher_attrib_info.email=account_email
            teacher_info.save()
            teacher_attrib_info.save()
            ret["success"]=1
            ret["reason"]=None
            return JsonResponse(ret)
        except:
            ret["success"] = 0
            ret["reason"] = "信息不符合要求"
            return JsonResponse(ret)





@csrf_exempt
def api_teacher_course(request):
    if request.method == "GET":
        print("=====")
        try:
            account_id = request.GET["account_id"]

            teacher_course=teach.objects.filter(teacher_id=account_id)
            print(teacher_course)
            course_list=[]
            for t in teacher_course:
                tmp={}
                course_id=course.objects.get(course_id=t.course_id)
                tmp["name"]=course_id.name
                tmp["credit"]=course_id.credit
                course_list.append(tmp)

            return JsonResponse(course_list)

        except Exception as e:
            print(e)
            return HttpResponseBadRequest()

@csrf_exempt
def api_teacher_addcourse(request):
    if request.method == "POST":
        try:
            id = request.POST["id"]
            name = request.POST["name"]
            credit = request.POST["credit"]
            intro = request.POST["intro"]
            hour=float(request.POST["hour"])


            new_course = course()
            new_course.id = id
            new_course.name = name
            new_course.credit = credit
            new_course.intro = intro
            new_course.hour=hour
            new_course.save()
            return JsonResponse({"success": 1, "reason": None})

        except:
            return HttpResponseBadRequest()

@csrf_exempt
def api_teacher_chgcourse(request):
    if request.method == "POST":
        try:
            id = request.POST["id"]
            name = request.POST["name"]
            credit = request.POST["credit"]
            hour=float(request.POST["hour"])
            intro = request.POST["intro"]

            tmp_course=course.objects.get(course_id=id)
            tmp_course.name = name
            tmp_course.credit = credit
            tmp_course.intro = intro
            tmp_course.hour=hour
            tmp_course.save()
            return JsonResponse({"success": 1, "reason": None})

        except:
            return HttpResponseBadRequest()
