from django.conf.urls import include, url
from django.contrib import admin

import basicInfo.api.account as api

urlpatterns = [
    # Examples:
    # url(r'^$', 'teachSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^account/login",api.api_account_post)
]
