from django.conf.urls import include, url
from django.contrib import admin

import basicInfo.api.account as api

urlpatterns = [
    # Examples:
    # url(r'^$', 'teachSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^account/login$",api.api_account_post),
    url(r"^account/register$",api.api_account_register_post),
    url(r"^account/repassword$",api.api_account_repassword_post),
    url(r"^account/person$",api.api_account_person),
    
]
