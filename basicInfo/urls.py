from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'teachSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^$", views.default),
    url(r"^login$", views.login),
    url(r"^signup$", views.signup),
    url(r"^student$", views.student),
    url(r"^teacher$", views.teacher),
    url(r"^exam$", views.exam),
    url(r"^calender$", views.calendar),
    url(r"^grade$", views.grade),
    url(r"^courseplan$", views.courseplan),
    url(r"^personalinfo$", views.personalinfo),
    url(r"^courseregist$", views.courseregist),
    url(r"^mycourse$", views.mycourse),
    url(r"^coursesearch$", views.coursesearch),
    url(r"^teacher_information$", views.teacher_information),
    url(r"^teacher_comment$", views.teacher_comment),
    url(r"^teacher_course_regist$", views.teacher_course_regist),
    url(r"^teacher_course_edit$", views.teacher_course_edit),
]
