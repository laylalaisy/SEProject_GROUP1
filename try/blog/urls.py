from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.default, name='index'),
    url(r'login*', views.login, name='login'),
    url(r'index*', views.index, name='index'),
    url(r'calender*', views.calendar, name='calender'),
    url(r'grade*', views.grade, name='grade'),
    url(r'exam*', views.exam, name='exam'),
    url(r'personinfo*', views.personinfo, name='personinfo'),
    url(r'CoursePlan*', views.CoursePlan, name='CoursePlan'),
    url(r'RegistLesson*', views.RegistLesson, name='RegistLesson'),
]
