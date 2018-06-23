from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponse

from basicInfo.models import account, examination, takeup, teach, course, room, learn, master, college

@csrf_exempt
def api_admin_judge(request):
    if request.method == "POST":
        try:
            id = request.POST["id"]
            accept = request.POST["accept"]

            tmp_course = course.objects.get(course_id=id)
            if accept:
                tmp_course.type = "普通课程"
                tmp_course.save()
            else:
                tmp_course.delete()
            return JsonResponse({"success": 1, "reason": None})

        except:
            return HttpResponseBadRequest()

@csrf_exempt
def api_admin_modify(request):
    if request.method == "POST":
        try:
            id = request.POST["id"]
            name = request.POST["name"]
            credit = request.POST["credit"]
            intro = request.POST["intro"]
            type = request.POST["type"]

            tmp_course = course.objects.get(course_id=id)
            tmp_course.name = name
            tmp_course.credit = credit
            tmp_course.intro = intro
            tmp_course.type = type
            tmp_course.save()
            return JsonResponse({"success": 1, "reason": None})

        except:
            return HttpResponseBadRequest()

@csrf_exempt
def api_admin_promote(request):
    if request.method == "POST":
        try:
            account_id = request.POST["account_id"]
            college_name = request.POST["college"]

            new_master = master()
            new_master.teacher_id = account_id
            new_master.college_id = college.objects.get(name=college_name)
            new_master.save()
            return JsonResponse({"success": 1, "reason": None})

        except:
            return HttpResponseBadRequest()

@csrf_exempt
def api_admin_college(request):
    if request.method == "GET":
        try:
            college_list = []
            for c in college.objects.get():
                tmp = {}
                tmp["name"] = c.name
                college_list.append(tmp)

            return JsonResponse(college_list)

        except:
            return HttpResponseBadRequest()

@csrf_exempt
def api_admin_addteach(request):
    if request.method == "POST":
        try:
            duplicate = request.POST["duplicate"]
            teacher_id = request.POST["teacher"]
            course_id = request.POST["course"]
            capacity = request.POST["capacity"]
            exam = request.POST["exam"]

            new_teach=teach()
            new_teach.duplicate = duplicate
            new_teach.teacher = teacher_id
            new_teach.course = course_id
            new_teach.capacity = capacity
            new_teach.exam = exam
            new_teach.save()
            return JsonResponse({"success": 1, "reason": None})

        except:
            return HttpResponseBadRequest()

@csrf_exempt
def api_student_info(request):
    if request.method == "POST":
        try:
            account_id = request.POST["account_id"]
            name=request.POST["name"]
            dorm=request.POST["dorm"]

            info=student.objects.get(student_id=account_id)
            info.name = name
            info.dorm = dorm
            info.save()

            return JsonResponse({"success": 1, "reason": None})

        except:
            return HttpResponseBadRequest()

@csrf_exempt
def api_teacher_info(request):
    if request.method == "POST":
        try:
            account_id = request.POST["account_id"]
            name=request.POST["name"]
            title=request.POST["title"]
            office=request.POST["office"]
            management=request.POST["management"]

            info=teacher.objects.get(teacher_id=account_id)
            info.name = name
            info.title = title
            info.office = office
            info.management = management
            info.save()

            return JsonResponse({"success": 1, "reason": None})

        except:
            return HttpResponseBadRequest()


