from django.shortcuts import render

# Create your views here.


def default(request):
    return render(request, 'login-home.html', {})


def signup(request):
    return render(request, "signup.html", {})


def login(request):
    return render(request, "login.html", {})


def student(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "student.html", feedDict)


def exam(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "exam.html", feedDict)


def calendar(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "calender.html", feedDict)


def courseplan(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "courseplan.html", feedDict)


def personalinfo(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "personinfo.html", feedDict)


def courseregist(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "courseregist.html", feedDict)



def mycourse(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "mycourse.html", feedDict)


def grade(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "grade.html", feedDict)


def coursesearch(request):
    sid = request.session["account_id"]
    feedDict={
        "account_id": sid
    }
    return render(request, "coursesearch.html", feedDict)


def teacher(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "teacher_index.html", feedDict)


def teacher_information(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "teacher_information.html", feedDict)


def teacher_comment(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "teacher_comment.html", feedDict)


def teacher_course_regist(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "teacher_course_regist.html", feedDict)


def teacher_course_edit(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "teacher_course_edit.html", feedDict)


def school_forum(request):
    tid = request.session["account_id"]
    feedDict={
        "account_id": tid
    }
    return render(request, "school_forum.html", feedDict)
