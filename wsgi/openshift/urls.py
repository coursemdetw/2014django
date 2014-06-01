from django.conf.urls import patterns, include, url

from django.contrib import admin
# 導入專案中的 views.py
import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # 利用所導入的 views.py 中的 index 方法來回應 url 連結
    url(r'^$', views.index, name='index'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

