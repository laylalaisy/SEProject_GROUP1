from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponse

from basicInfo.models import account, examination, takeup, teach, course, room, learn, master, college,student,teacher,readyteach

import traceback

@csrf_exempt
def api_admin_coursewaitlist(request):

    if request.method=="GET":
        try:
            allret=[]
            wait_courses=readyteach.objects.all()
            for wait_course in wait_courses:
                '''
                id(string):课程号
                num(string):开课次数
                examdate(string):考试日期
                tid(string):教师工号
                capacity(string):课程容量
                name(string)
                '''
                print("------")
                ret = {}
                ret["id"]=str(wait_course.course_id.course_id)
                print("id",ret)
                ret["num"]=str(wait_course.course_id.duplicate)
                #ret["examdate"]=
                ret["tid"]=str(wait_course.teacher_id.teacher_id.account_id)
                ret["name"] = wait_course.course_id.name
                ret["capacity"]=str(wait_course.capacity)
                ret["name"]=wait_course.course_id.name
                allret.append(ret)
            sorted(allret,key=lambda x:int(x["id"]))
            return JsonResponse(allret,safe=False)
        except Exception as e:
            print(e)
            traceback.print_exc()
            return JsonResponse([],safe=False)
    return HttpResponseBadRequest()
    pass

@csrf_exempt
def api_admin_agreecourse(request):
    if request.method=="POST":
        course_id=request.POST["courseid"]
        teacher_id=request.POST["teacherid"]
        ret={"success":0,
             "reason":None
             }
        try:
            waitCourses=readyteach.objects.filter(course_id=course_id,teacher_id=teacher_id)
            for waitCourse in waitCourses:
                teachobj=teach()
                teachobj.course_id=waitCourse.course_id
                teachobj.teacher_id=waitCourse.teacher_id
                teachobj.capacity=waitCourse.capacity
                teachobj.save()
                waitCourse.course_id.duplicate+=1
                waitCourse.course_id.save()
                waitCourse.delete()
                break
            ret["success"]=1

            return JsonResponse(ret)
        except Exception as e:
            print(e)
            traceback.print_exc()
            ret["reason"]="没有改课"
            return JsonResponse(ret)
    return HttpResponseBadRequest()



@csrf_exempt
def api_admin_modify_course(request):
    if request.method == "POST":
        try:
            pre_id = request.POST["pre_id"]
            post_id=request.POST["post_id"]

            name = request.POST["name"]
            credit = request.POST["credit"]
            intro = request.POST["intro"]
            type = request.POST["type"]

            if pre_id==post_id:
                tmp_course = course.objects.get(course_id=pre_id)
            else:
                tmp_course=course.objects.get(course_id=pre_id)
                tmp_course.delete()
                tmp_course=course()
                tmp_course.course_id_1=post_id
            tmp_course.name = name
            tmp_course.credit = credit
            tmp_course.intro = intro
            tmp_course.type = type
            tmp_course.save()
            return JsonResponse({"success": 1, "reason": None})

        except:
            return HttpResponseBadRequest()

@csrf_exempt
def api_admin_modify_teach(request):
    if request.method == "POST":
        try:
            id = request.POST["teach_id"]

            teacher=request.POST["teacher"]

            capacity=request.POST["capacity"]

            teach_info=teach.objects.get(teach_id=id)
            teach_info.capacity=capacity
            teach_info.teacher_id=teacher
            teach_info.save()

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
            teacher_info=teacher.objects.get(teacher_id=account_id)
            teacher_info.management=college_name
            teacher_info.save()

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
            return JsonResponse({"success": 0, "reason": "没有这个学生"})
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
            return JsonResponse({"success": 0, "reason": "没有这个老师"})
    return HttpResponseBadRequest()


