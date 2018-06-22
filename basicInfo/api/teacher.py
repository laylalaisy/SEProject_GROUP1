from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponse

from basicInfo.models import account, examination, takeup, teach, course, room, learn

@csrf_exempt
def api_teacher_course(request):
    if request.method == "GET":
        try:
            account_id = request.GET["account_id"]

            teacher_course=teach.objects.filter(teacher_id=account_id)

            course_list=[]
            for t in teacher_course:
                tmp={}
                course_id=course.objects.get(course_id=t.course_id)
                tmp["name"]=course_id.name
                tmp["credit"]=course_id.credit
                course_list.append(tmp)

            return JsonResponse(course_list)

        except:
            return HttpResponseBadRequest()

@csrf_exempt
def api_teacher_addcourse(request):
    if request.method == "POST":
        try:
            id = request.POST["id"]
            name = request.POST["name"]
            credit = request.POST["credit"]
            intro = request.POST["intro"]

            new_course = course()
            new_course.id = id
            new_course.name = name
            new_course.credit = credit
            new_course.intro = intro
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
            intro = request.POST["intro"]

            tmp_course=course.objects.get(course_id=id)
            tmp_course.name = name
            tmp_course.credit = credit
            tmp_course.intro = intro
            tmp_course.save()
            return JsonResponse({"success": 1, "reason": None})

        except:
            return HttpResponseBadRequest()
