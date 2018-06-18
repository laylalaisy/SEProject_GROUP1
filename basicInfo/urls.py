from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'teachSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^$",views.default),
    url(r"^login$",views.login),
    url(r"^signup$",views.signup),
    url(r"^student$",views.student),
    url(r"^teacher$",views.teacher)
]
