from django.conf.urls import url, include
from . import views


urlpatterns = [
    # url(r'^$', views.?, name='?'),
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
    url(r"^admin$", views.admin),
    url(r"^admin_information$", views.admin_information),
    url(r"^admin_comment$", views.admin_comment),
    url(r"^admin_course_regist$", views.admin_course_regist),
    url(r"^admin_course_edit$", views.admin_course_edit),
    url(r"^admin_course_approve$", views.admin_course_approve),
    url(r"^admin_course_adjust$", views.admin_course_adjust),
    url(r"^admin_apply_approve_s$", views.admin_apply_approve_s),
    url(r"^admin_apply_approve_t$", views.admin_apply_approve_t),
    url(r"^admin_select_adjust$", views.admin_select_adjust),
]
