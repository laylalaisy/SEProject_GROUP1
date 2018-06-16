from django.conf.urls import include, url
from django.contrib import admin
import basicInfo.urls
import basicInfo.apiUrls

urlpatterns = [
    # Examples:
    # url(r'^$', 'teachSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r"^basic/",include(basicInfo.urls)),
    url(r"^api/",include(basicInfo.apiUrls))
]
