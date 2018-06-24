from django.shortcuts import render

# Create your views here.


def default(request):
    return render(request, 'basicInfo/login-home.html', {})


def signup(request):
    return render(request, "basicInfo/signup.html", {})


def login(request):
    return render(request, "basicInfo/login.html", {})


def student(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "basicInfo/student.html", feedDict)


def exam(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "basicInfo/exam.html", feedDict)


def calendar(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "basicInfo/calender.html", feedDict)


def courseplan(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "basicInfo/courseplan.html", feedDict)


def personalinfo(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "basicInfo/personinfo.html", feedDict)


def courseregist(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "basicInfo/courseregist.html", feedDict)



def mycourse(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "basicInfo/mycourse.html", feedDict)


def grade(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "basicInfo/grade.html", feedDict)


def coursesearch(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "basicInfo/coursesearch.html", feedDict)


def teacher(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/teacher_index.html", feedDict)


def teacher_information(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/teacher_information.html", feedDict)


def teacher_comment(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/teacher_comment.html", feedDict)


def teacher_course_regist(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/teacher_course_regist.html", feedDict)


def teacher_course_edit(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/teacher_course_edit.html", feedDict)


def school_forum(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/school_forum.html", feedDict)

def admin(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/admin_index.html", feedDict)


def admin_information(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/admin_information.html", feedDict)

def admin_comment(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/admin_comment.html", feedDict)


def admin_course_regist(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/admin_course_regist.html", feedDict)


def admin_course_edit(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/admin_course_edit.html", feedDict)

def admin_course_approve(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/admin_course_approve.html", feedDict)

def admin_course_adjust(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/admin_course_adjust.html", feedDict)


def admin_apply_approve_s(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/admin_apply_approve_s.html", feedDict)

def admin_apply_approve_t(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/admin_apply_approve_t.html", feedDict)


def admin_select_adjust(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "basicInfo/admin_select_adjust.html", feedDict)



